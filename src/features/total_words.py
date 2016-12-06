#####################################################
#COUNTING THE NUMBER OF TOTAL WORDS#
#####################################################

def fill_total_words_column(train_df, valid_df):
    #Total number of words
    total_number_train = []
    total_number_valid = []

    for i in range(len(train_df)):
        splits = train_df.iloc[i]["essay"].split()
        total_words = len(splits)
        total_number_train.append(total_words)

    for i in range(len(valid_df)):
        splits = valid_df.iloc[i]["essay"].split()
        total_words = len(splits)
        total_number_valid.append(total_words)

    train_df["total_words"] = total_number_train
    valid_df["total_words"] = total_number_valid

    train_df, valid_df = util.append_standardized_column(train_df, valid_df, 'word_count')

    return train_df, valid_df
