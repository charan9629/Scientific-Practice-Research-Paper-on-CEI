# Datasets

## Overview

This folder contains the datasets used in the research study:

**"Conference Excellence Index (CEI): A Multi-Dimensional Framework for Evaluating IoT Conferences"**

The dataset was compiled as part of the Scientific Practice course at the University of Bremen and contains bibliometric information collected from major Internet of Things (IoT) conference proceedings published during 2023 and 2024. Data from the 2023 conference editions were collected in 2025, while data from the 2024 conference editions were collected in 2026.

---

## Dataset File

### Organised_Data_Sets.xlsx

This Excel workbook contains the consolidated conference and publication data used for analysis, normalization, ranking, and visualization.

---

## Data Sources

The dataset was created from conference proceedings, publisher websites, digital libraries, and publicly available bibliometric information.

Conferences included in the study:

* BIOTC
* DCOSS-IoT
* EAI HealthyIoT
* EWSN
* ICIOT
* IFIP-IoT
* IoTBDS
* IoTSMS
* SenSys
* WF-IoT

---

## Workbook Structure

### Sheet: total_consolidated_data

Contains paper-level information for all collected conference publications.

Typical attributes include:

* Conference Name
* Conference Year
* Paper Title
* Number of Authors
* First Author Country
* Number of References
* Number of Citations (Google Scholar)
* Number of Tables
* Number of Figures

This sheet serves as the primary source for citation distribution analysis and conference statistics.

---

### Sheet: statistical_evaluation

Contains conference-level aggregated metrics and normalized scores.

Attributes include:

* Average Citations
* Average References
* Average Authors
* Average Graphs and Tables
* Citation Impact Score
* Diversity Score
* Reference Quality Score
* Collaboration Score
* Visual Communication Score
* CEI Score

This sheet is used for conference ranking and comparative analysis.

---

## Data Preprocessing

The following preprocessing steps were performed before analysis:

1. Conference name standardization.
2. Duplicate record removal.
3. Missing data validation.
4. Integration of missing conference editions.
5. Calculation of conference-level averages.
6. Normalization of evaluation metrics.

---

## Usage

The dataset supports:

* Bibliometric analysis
* Conference ranking studies
* Citation analysis
* Collaboration analysis
* Diversity assessment
* Visualization generation
* CEI score computation

---

## Reproducibility

All figures, tables, rankings, and statistical analyses presented in the paper are generated directly from the data contained in this workbook. The dataset is structured to ensure reproducibility of the reported results.
