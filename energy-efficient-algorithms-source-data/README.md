# Source data for Figures 5 and 6 and the Section 14 worked example

**Paper:** Energy-efficient algorithms and sustainable computing: a theoretical framework for reducing computational energy cost and environmental impact

**Authors:** Chris Gilbert, Duah Jeremiah Leakpor, Kwitee D. Gaylah and John K. Constance  
**Contact:** the corresponding author named in the paper

These files contain the numbers behind two illustrative figures and the worked calculation in Section 14 of the paper. The paper is a theoretical framework. Its figures are illustrative, and none of the values were measured in an experiment. They are published so that readers can check the figures and the arithmetic. The dataset contains no personal data.

## Files

- `figure5_energy_accuracy_values.csv`: approximate values for the two series in Figure 5 at six levels of allowed approximation error (epsilon). Columns: epsilon; energy_index_digitised (relative energy cost, index units); accuracy_percent_digitised (accuracy in per cent); note.
- `figure6_energy_carbon_values.csv`: energy (kWh) and carbon (kgCO2e) for Algorithm A and Algorithm B, as labelled in Figure 6. Carbon is energy multiplied by 0.45 kgCO2e per kWh. The two digitised columns are the bar heights read from the figure.
- `section14_worked_example.csv`: each quantity in the Section 14 calculation, with its formula.
- `figure5.png`: the Figure 5 image as published, 1624 by 962 pixels.
- `digitise_figure5.py`: Python script (needs numpy and Pillow). It calibrates the axes from the tick marks and reports the centre of each marker in figure5.png. Run it with: `python3 digitise_figure5.py figure5.png`

## How the values were obtained

**Figure 5.** The original plotting values were not available, so each value was read from the pixel positions in figure5.png. The tick marks give a linear calibration for each axis, with residuals of at most 0.5 pixels. Both series use the same blue, so circles (energy) and squares (accuracy) were told apart by shape. At epsilon = 0.01 and 0.20 the square covers the circle, and at epsilon = 0.02 the two markers touch. For these three points the centres were located from the visible edges, as noted in the note column. The energy values at these points are the least certain. The estimated uncertainty is about 0.2 index points for energy and 0.1 percentage points for accuracy.

**Figure 6 and Section 14.** The energies (2.5 and 1.6 kWh) and the carbon intensity (0.45 kgCO2e per kWh) are the values stated in Section 14. The carbon values follow from these: 2.5 × 0.45 = 1.125 and 1.6 × 0.45 = 0.72 kgCO2e. The bar heights read from Figure 6 agree with these values to within 0.01.

## Limitations

- The values are illustrative. They do not describe any real algorithm, system or measurement.
- The Figure 5 values were read from the image, so they may differ slightly from the numbers used to draw it. If the original plotting script or spreadsheet can be found, its values should replace the digitised values in this dataset.

## Licence and citation

**Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0).

**Suggested citation:** Gilbert, C., Leakpor, D. J., Gaylah, K. D. and Constance, J. K. (2026). Source data for Figures 5 and 6 and the Section 14 worked example in "Energy-efficient algorithms and sustainable computing: a theoretical framework for reducing computational energy cost and environmental impact". Available at: https://github.com/chrisgilbertp/chrisgilbertp/tree/main/energy-efficient-algorithms-source-data

Version 2, 10 October 2026.
