一.EV3程式碼為繪圖機器人

可以讀取SVG圖片檔的向量

並且判斷圖片的周圍線條

畫出該圖片

原始圖片

![images](https://github.com/valosz66666/PythonCode/blob/master/images/EV3.PNG)

最後畫出的圖片
![images](https://github.com/valosz66666/PythonCode/blob/master/images/EV3%E6%88%90%E5%93%81.PNG)

Demo網址:https://www.youtube.com/watch?v=VowhaPzoviE

二.kafka

kafka_consumer.py 為kafka的consumer 傳送資料至topic內

kafka_producer.py 為kafka的producer 定時將topic資料寫入至kafka內

三.web_crawler

包含爬YouTube留言、頻道、搜尋列表，IG的圖片跟影片，各大新聞網的爬蟲程式。


四.VGG16

搜尋並隨機爬取67張正濱漁港的圖片

pic_similarity.py 為使用VGG16套件來將資料夾內所有圖片做乘積的運算，取得特徵值分數最高的圖片。可以做為該搜尋的代表圖片。


五.其他程式碼

multiple_category.py 將文字斷詞後轉換成稀疏矩陣做訓練的多元分類器程式碼

news_wordcloud_by_day.py 將新聞做成文字雲的程式碼

nnws_similarity.py 將每日新聞用文字相似度做計算，可以用來判斷某個議題的週期

word_classifier_jiebacut.py 將字典內的詞轉換成稀疏矩陣以後做分群，把類似的資料放在同一組

