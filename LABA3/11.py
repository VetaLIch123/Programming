ukr_letters = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
ukr_letters_trans = ukr_letters[20:] + ukr_letters[:20]
trans_table = str.maketrans(ukr_letters_trans, ukr_letters)
message = 'еєджзц бєрмц, ґюш жбврхґц.'
decoded_text = message.translate(trans_table)
print(decoded_text)
