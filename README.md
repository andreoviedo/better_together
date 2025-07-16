# Replication files for "Better Together? Estimating the Effect of Multiple Borrowers on Mortgage Default Risk Using Double Machine Learning"

Author: Andre Oviedo Mendoza, CFA

## Introduction

This final project write-up investigates the effect of multiple borrowers on mortgage default risk using double machine learning. 
By using this approach, we can account for complex relationships between variables while producing consistent and asymptotically normal estimates of treatment effects. We find that having multi-
ple borrowers at origination is associated with a lower probability of default of around -1.6 percentage points. 
This is consistent with the findings of previous research that suggests that multiple borrowers can create a collective risk mitigation mechanism that enhances overall loan repayment probability. 
This result is robust to different models and control variables.

## Data

- Source: Freddie Mac Single-Family dataset
- Information from 2011 to 2016 on 96M loans
- Chose to work with a sample of 306K loans (from IL) to speed up computation
- Information on origination and performance. Around 100 variables available for each loan.
- Choice of covariates focused on borrower and loan characteristics

Really high quality data which is not only updates new information but also checks for
errors in past publications.

DISCLAIMER: Data frorm Freddie Mac is not uploaded in this repo due to copyrights. You can download it from the source and use the python files to replicate the whole dataset creation

