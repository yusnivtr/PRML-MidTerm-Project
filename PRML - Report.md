# 1. Project Overview

Project **Mental Attention States Classification Using EEG Data**, classify mental attention states (focused, unfocused, drowsy) based on EEG signals using machine learning techniques.

## 1.1. What is EEG?

EEG (Electroencephalogram) is a method of measuring and recording the electrical activity of the brain through electrodes placed on the scalp. These electrical signals reflect the activity of nerve cells in the brain as they transmit information. EEG is commonly used in medicine to diagnose neurological disorders such as epilepsy, dementia, or sleep-related issues, as well as in brain research. The EEG signals are recorded as brain waves with different frequencies and amplitudes, which can be categorized into types such as alpha, beta, delta, and theta waves.

## 1.2. Experiment in project

The experiments were conducted between 6 PM and 7 PM. The details of the experiments are given below (Authors):

Participants controlled a simulated passenger train over a primarily featureless route for a duration of 35 to 55 minutes. Specifically, during the first 10 minutes of each experiment, the participants were engaged in focused control of the simulated train, paying close attention to the simulator’s controls, and following the developments on the screen in detail. During the second 10 minutes of the experiments, the participants stopped following the simulator and became de-focused. The participants did not provide any control inputs during that time and stopped paying attention to the developments on the computer screen; however, they were not allowed to close their eyes or drowse. Finally, during the third 10 minutes of the experiments, the participants were allowed to relax freely, close their eyes and doze off, as desired.

### Experiment pitfall

The experiment only had 5 subjects, and had been conducted for 7 days. Each record contains one EEG data each subject each day, except for one, who didn't joined in the last day. Hence, there are 7 \* 5 - 1 =34 records in total.

Since there are only 5 subjects, the data is hugely biased toward them. If you want to use the result in this report to generalize further, please use it with caution.

## 1.3. Dataset

The dataset used in this study is available for access on Kaggle. It is titled "EEG Data for Mental Attention State Detection" and contains various records related to EEG signals, specifically designed to analyze mental attention states. You can access and download the dataset using the following link: [EEG Data for Mental Attention State Detection on Kaggle](https://www.kaggle.com/datasets/inancigdem/eeg-data-for-mental-attention-state-detection/data).

This dataset consists of 34 experiments designed to monitor the attention state of human participants using passive EEG BCI (Brain-Computer Interface). Each Matlab file in the dataset contains data acquired from an EMOTIV device during a single experiment. The raw data is stored in the variable `o.data`, which is an array of size {number-of-samples} x 25. Each column of `o.data` (i.e., `o.data(:,i)`) corresponds to one data channel.

The sampling frequency of the data is 128 Hz. In `o.data`, it has the list of columns provided below:

| ID   | Channel Name        | Meaning                                                |
| ---- | ------------------- | ------------------------------------------------------ |
| 1    | `'ED_COUNTER'`      | Counter for collected data samples.                    |
| 2    | `'ED_INTERPOLATED'` | Data interpolation state.                              |
| 3    | `'ED_RAW_CQ'`       | Raw data quality from sensors.                         |
| 4–17 | EEG Channels        | Channels containing EEG data (electroencephalography). |
| 18   | `'ED_GYROX'`        | Data from gyroscope sensor (X-axis).                   |
| 19   | `'ED_GYROY'`        | Data from gyroscope sensor (Y-axis).                   |
| 20   | `'ED_TIMESTAMP'`    | Timestamp.                                             |
| 21   | `'ED_ES_TIMESTAMP'` | Event timestamp.                                       |
| 22   | `'ED_FUNC_ID'`      | Function ID code.                                      |
| 23   | `'ED_FUNC_VALUE'`   | Function value.                                        |
| 24   | `'ED_MARKER'`       | Event marker.                                          |
| 25   | `'ED_SYNC_SIGNAL'`  | Synchronization signal.                                |

The experiment was conducted with 5 participants, each performing the experiment over a 7-day period. However, the last participant only completed the experiment in 6 days, resulting in a total of 34 files. Typically, during the first two days, participants familiarize themselves with the experimental process, which makes the data from these two days relatively complex. The data from the following 5 days are more stable. The EEG data we focus on comes primarily from the EEG channels, where the EEG data is stored.

## 1.4. Main stages of the project

This project includes the following main stages: **EDA** (Exploratory Data Analysis), **data preprocessing**, **feature extraction**, **modeling**, and **model evaluation**. In the preprocessing stage, we use a bandpass filter, re-referencing method, and ICA (Independent Component Analysis). For feature extraction, we apply Fourier Transform to convert the data from the time-domain to the frequency-domain in order to extract relevant features.

> ... Viết tiếp phần modeling, cách đánh giá model (overview thôi)

# 2. Data Preprocessing

After extracting data from 14 channels by converting the Matlab files, we proceeded with data processing and filtering. We first applied a high-pass filter, followed by re-referencing using the Common Average Reference (CAR) method. Finally, we used Independent Component Analysis (ICA) to remove noise sources such as blink and muscle artifacts, and employed the LOF (Local Outlier Factor) algorithm for further refinement.

## 2.1. High-pass filter

A high-pass filter allows signals with a frequency higher than a certain cutoff frequency to pass through, while attenuating frequencies lower than the cutoff. The mathematical basis for designing a high-pass filter often involves using the **Butterworth filter** design, which is known for providing a maximally flat frequency response in the passband.

> Không biết nói gì tiếp luôn

## 2.2. Re-reference (Common Average Reference)

**Re-referencing** is a preprocessing technique used to improve the quality and consistency of EEG signals by eliminating certain common sources of noise or artifact. In particular, **Common Average Reference (CAR)** is a method where the reference electrode is replaced by the average of all EEG channels in the dataset.

The idea behind CAR is that, in most EEG experiments, all electrodes are measuring similar common-mode noise (e.g., power line interference, or drift). By subtracting the mean of all electrode signals from each individual channel, the common noise is effectively removed, which enhances the signal related to the brain's activity.

For an EEG signal consisting of multiple channels, the **Common Average Reference (CAR)** is computed as the mean of all channels:

$$
\text{CAR} = \frac{1}{N}\sum_{i=1}^{N}x_i
$$

Where:

- $x_i$​ is the signal from the $i$-th channel.
- $N$ is the total number of channels.
- $\text{CAR}$ is the average of all channels' signals.

Each channel's signal is then re-referenced by subtracting the average reference from it:

$$
x'_i = x_i - \text{CAR}
$$

This method ensures that any common-mode artifacts (such as power line noise) are minimized, making the analysis of brain activity more accurate. The approach is widely used in EEG preprocessing to reduce the impact of external interferences that could distort the underlying neural signals.

## 2.3. Independent Component Analysis

This is used to extract independent components from a signal, which is brain wave in our case. Our hypothesis is the artifact and the underlying brain wave are mixed together, but they are independent on each other, hence we can use ICA to separate them apart.

The artifacts includes, but does not limit to: Heartbeat (ECG), eyeball movement (EOG), muscle movement, cable movement, sweat.

> Include images here

However, since ICA is a signal processing algorithm, not a brainwave processing algorithm, it can't tell artifacts and brainwave apart automatically for us. We need to categorize do it manually, or use other algorithms to do it. Because of our short of domain knowledge timeline and immense amount of images needed to be reviewed, we decided to use algorithms. The documentation can be found at MNE python

> Include links here

# 3. Feature Extraction

After the data preprocessing step, we applied Fast Fourier Transform (FFT) to convert the data from the time domain to the frequency domain, enabling the extraction of relevant features from the data.

## 3.1. Fourier Transform

We can take a series of sine waves and assign each sine wave a different amplitude, frequency, and phase. By summing these sine waves together, we can obtain a more complex signal. However, in practical data analysis, we face the opposite problem: we start with a more complex signal and want to determine which sine waves, frequencies, amplitudes, and phases can be used to represent this signal. This problem is particularly important for EEG data, which contains overlapping frequencies. So, how can we identify which frequencies are present in the signal, with what intensity, and at what times? Fortunately, Fourier comes to our rescue. Fourier provided us with an algorithm to analyze such signals, and Fourier’s theorem states that any signal can be represented as a combination of different sine waves, each with its own amplitude, frequency, and phase. One of the powerful aspects of the Fourier transform is that it works perfectly with any signal, not just those made of pure sine waves. Any signal can be represented as a combination of different sine waves.