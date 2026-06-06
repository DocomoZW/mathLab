#!/bin/bash
# Batch render all 14 AL2 Trigonometry animation scenes as GIFs

ANIM_DIR="/opt/data/.hermes/content/animations/a_level/AL2_Trigonometry"
OUT_DIR="/opt/data/.hermes/content/gifs/igcse_o"
MEDIA_DIR="/tmp/manim_al2"

MANIM_CMD="/opt/data/.local/bin/micromamba run -p /opt/data/.local/manim-env python3 -m manim render -ql --format gif --progress_bar none --media_dir ${MEDIA_DIR} --fps 8 -r 426,240"

declare -A SCENES
SCENES["AL2_Q1_circular_measure.py"]="ArcLengthSector RadianConversion"
SCENES["AL2_Q2_trig_basics.py"]="TrigGraphs ExactValues"
SCENES["AL2_Q3_trig_identities.py"]="PythagoreanIdentity TrigIdentityProof"
SCENES["AL2_Q4_trig_equations.py"]="CASTDiagram QuadraticTrigEquations"
SCENES["AL2_Q5_angle_transformations.py"]="CompoundAngleFormulas RForm"
SCENES["AL2_Q6_differentiation_of_trig.py"]="DerivativeTrigRules TangentToTrigCurve"
SCENES["AL2_Q7_integration_of_trig.py"]="IntegrationTrigRules IntegratePowersTrig"

SUCCESS=0
FAIL=0

echo "=== Starting AL2 Trigonometry GIF Rendering ==="
echo ""

for FILE in "${!SCENES[@]}"; do
    SCENE_LIST=${SCENES[$FILE]}
    for SCENE in $SCENE_LIST; do
        echo "--- Rendering ${SCENE} from ${FILE} ---"
        cd "$ANIM_DIR" && $MANIM_CMD "$FILE" "$SCENE" 2>&1 | tail -5
        if [ $? -eq 0 ]; then
            FOUND_GIF=$(find "${MEDIA_DIR}" -name "${SCENE}_ManimCE_v0.20.1.gif" -type f 2>/dev/null | head -1)
            if [ -z "$FOUND_GIF" ]; then
                FOUND_GIF=$(find "${MEDIA_DIR}" -name "${SCENE}.gif" -type f 2>/dev/null | head -1)
            fi
            if [ -n "$FOUND_GIF" ]; then
                cp "$FOUND_GIF" "${OUT_DIR}/${SCENE}.gif"
                echo "Copied to ${OUT_DIR}/${SCENE}.gif"
                SUCCESS=$((SUCCESS + 1))
            else
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
