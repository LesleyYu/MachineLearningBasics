
# calculate metrics
# def Calc_metrics(model):
#     metrics = {}
#     for y in y_labels_train:
#         # train the final model
#         model.fit(X_train, y)
#         # predictions
#         y_pred_train = model(X_train)
#         y_pred_test = model(X_test)
#         # train
#         EMscore_train = accuracy_score(y, y_pred_train)# Exact Match    # WRONG
#         HLscore_train = hamming_loss(y, y_pred_train)# Haaming Loss
#         #test
#         EMscore_test = accuracy_score(y, y_pred_test)# Exact Match 
#         HLscore_test = hamming_loss(y, y_pred_test)# Haaming Loss

#         metrics[y.name] = [EMscore_train, HLscore_train, EMscore_test, HLscore_test]

#     metrics.index = ['Exact Match(Train)', "Hamming Los(Train)", 'Exact Match(Test)', "Hamming Loss(Test)"]
#     metrics = pd.DataFrame(data = metrics)
#     display(metrics) # ???
#     return metrics
