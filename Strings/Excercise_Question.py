# Extract 0.8475 from the given string and convert it to float
# "X-DSPAM-Confidence: 0.8475 "

string = "X-DSPAM-Confidence: 0.8475 "
fpos = string.find(':')
print(fpos)
number_piece = string[fpos+1:]
print(number_piece)
number_piece = float(number_piece)
print(number_piece)
