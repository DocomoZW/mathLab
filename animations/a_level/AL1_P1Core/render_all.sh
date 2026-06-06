#!/bin/bash
# Batch render all 14 AL1 animation scenes as GIFs

ANIM_DIR="/opt/data/.hermes/content/animations/a_level/AL1_P1Core"
OUT_DIR="/opt/data/.hermes/content/gifs/igcse_o"
MEDIA_DIR="/tmp/manim_al1"

MANIM_CMD="/opt/data/.local/bin/micromamba run -p /opt/data/.local/manim-env python3 -m manim render -ql --format gif --progress_bar none --media_dir ${MEDIA_DIR} --fps 8 -r 426,240"

declare -A SCENES
SCENES["AL1_Q1_quadratics.py"]="CompSquare DiscriminantNature"
SCENES["AL1_Q2_functions.py"]="FunctionMap GraphTrans"
SCENES["AL1_Q3_coordinate_geometry.py"]="CircleEquation TangentCircle"
SCENES["AL1_Q4_binomial.py"]="PascalsTriangle BinomialTerm"
SCENES["AL1_Q5_series.py"]="ArithmeticVisual GeometricVisual"
SCENES["AL1_Q6_partial_fractions.py"]="PartialFracIntro FactorisationMethod"
SCENES["AL1_Q7_proof.py"]="DirectProof ContradictionProof"

SUCCESS=0
FAIL=0

for FILE in "${!SCENES[@]}"; do
    SCENE_LIST=${SCENES[$FILE]}
    for SCENE in $SCENE_LIST; do
        echo "--- Rendering ${SCENE} from ${FILE} ---"
        cd "$ANIM_DIR" && $MANIM_CMD "$FILE" "$SCENE" 2>&1 | tail -5
        if [ $? -eq 0 ]; then
            # Find and copy the GIF
            FOUND_GIF=$(find "${MEDIA_DIR}" -name "${SCENE}_ManimCE_v0.20.1.gif" -type f 2>/dev/null | head -1)
            if [ -z "$FOUND_GIF" ]; then
                FOUND_GIF=$(find "${MEDIA_DIR}" -name "${SCENE}.gif" -type f 2>/dev/null | head -1)
            fi
            if [ -n "$FOUND_GIF" ]; then
                cp "$FOUND_GIF" "${OUT_DIR}/${SCENE}.gif"
                echo "Copied to ${OUT_DIR}/${SCENE}.gif"
                SUCCESS=$((SUCCESS + 1))
            else
                # Try alternative name
                ALT_GIF=$(find "${MEDIA_DIR}" -name "*.gif" -newer "$ANIM_DIR/$FILE" -type f 2>/dev/null | head -1)
                if [ -n "$ALT_GIF" ]; then
                    cp "$ALT_GIF" "${OUT_DIR}/${SCENE}.gif"
                    echo "Copied alt to ${OUT_DIR}/${SCENE}.gif"
                    SUCCESS=$((SUCCESS + 1))
                else
                    echo "ERROR: Could not find GIF for ${SCENE}"
                    FAIL=$((FAIL + 1))
                fi
            fi
        else
            echo "ERROR: Failed to render ${SCENE}"
            FAIL=$((FAIL + 1))
        fi
        echo ""
    done
done

echo "=== Summary ==="
echo "Success: ${SUCCESS}, Failed: ${FAIL}"
echo "GIFs in: ${OUT_DIR}"
