import mymodule.stats_word
import codecs

fileHandler = open('tang300.json', mode='r', encoding='UTF-8')
report_lines = fileHandler.readlines()
log = "".join(report_lines)
mymodule.stats_word.stats_text_cn(log)

counter=100
print("""---唐诗300首中词频最高的前100个字---""")
