# txt="machine learning"
# wrd_lst=txt.split()
# print(wrd_lst)
#
# srt_frm=""
# for i in wrd_lst:
#  srt_frm=srt_frm+i[0].upper()
# print(srt_frm)

def genarator (sent):
 wrd_lst = sent.split()
 srt_frm=""
 for i in wrd_lst:
  srt_frm=srt_frm+i[0].upper()
 print(srt_frm)

txt=input("Enter Sentence:")
genarator(txt)