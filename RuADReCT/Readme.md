## Description

This dataset contains 9515 tweets on the health topic. Each tweet labeled whether tweet’s text contains information about adverse drug reactions of medication. Since the policy of Twitter does not allow the storing and publication of tweet texts in the public domain, the corpus consists of a file containing the tweet’s id, the class number, and a script to collect tweet’s text.

The dataset was created for the Social Media Mining for Health Applications (#SMM4H) Shared Task 2020 (https://healthlanguageprocessing.org/smm4h-sharedtask-2020/), which involves distinguishing tweets that report an adverse effect of medication from those that do not. The providers of the dataset are UPenn HLP Center (https://healthlanguageprocessing.org/) and CIMM KFU lab (https://cimm.site/, https://kpfu.ru/). 

## Archive structure

task2_ru_train.tsv - training data 
task2_ru_validation.tsv - vlidation data
task2_ru_test.tsv - test data
download_tweets.py - script to download tweets

## Annotation guidelines

Each tweet labeled whether tweet’s text contains information about adverse drug reactions of medication (label=1), or not (label=0).

The general rules for marking a tweet as positive for containing a mention of an ADR are:
1. The user states an ADR that resulted from taking the drug.
2. The ADR mentioned had been personally experienced by the user, or by someone known personally to the user.
3. The ADR mentioned is specific, that is it refers to a sign or symptom that can be coded to a medical term even if the mention itself is in colloquial terms.
4. The ADR occurred over the normal course of treatment and is not an effect from taking too much of the drug.
5. The ADR is not the result of taking two, or more, drugs at the same time (drug-drug interactions).

## Run script for download tweets

1. Get "access_token", "access_token_secret", "consumer_key", "consumer_secret" values following steps:
	1.1 Go to https://dev.twitter.com/apps/new and log in, if necessary
	1.2 Create an app by filling the required fields
	1.3 Go to the API Keys tab, there you will find your Consumer key, Consumer secret key, Access token, and Access token secret.
   See more details on https://developer.twitter.com/en/docs/basics/getting-started
2. Add obtained values to the corresponding fields of "token" value in the source code 
3. Run command: python download_tweets.py --input="path/to/input/file" --output="path/to/output/file"

## Citation

Ari Klein, Ilseyar Alimova, Ivan Flores, Arjun Magge, Zulfat Miftahutdinov, Anne-Lyse Minard, Karen O’Connor, Abeed Sarker, Elena Tutubalina, Davy Weissenbacher, and Graciela Gonzalez-Hernandez. 2020. Overview of the fifth Social Media Mining for Health Applications (#SMM4H) Shared Tasks at COLING 2020. In Proceedings of the Fifth Social Media Mining for Health Applications (#SMM4H) Workshop & Shared Task.

## Contacts

if you have any questions, feel free to write Elena Tutubalina (tutubalinaev@gmail.com), Ilseyar Alimova (alimovailseyar@gmail.com).

## Additional info

If you find this dataset helpful, also see The Russian Drug Reaction Corpus and Neural Models for Drug Reactions and Effectiveness Detection in User Reviews (https://github.com/cimm-kzn/RuDReC, https://doi.org/10.1093/bioinformatics/btaa675, https://arxiv.org/abs/2004.03659).