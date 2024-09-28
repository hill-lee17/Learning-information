# coding: utf-8

import sys
import re

import jieba
from sklearn import metrics
import joblib
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import MultinomialNB

def calssify(text):
    # Multinomial Naive Bayes Classifier
    clf = MultinomialNB()
    clf = joblib.load('model/'+str(type(clf))[8:-2]+'.model')


    with open('dict/stopwords.txt', 'r',encoding='UTF-8') as f:
        stopwords = list([w.strip() for w in f])
    #v = HashingVectorizer(non_negative=True, stop_words=stopwords, n_features=30000)
    v = HashingVectorizer(stop_words=stopwords, n_features=30000)

    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    text = ' '.join(jieba.cut(text, cut_all=False))
    text = re.sub(u'[$^()-=~！@#￥%……&*（）——+·{}|：“”《》？【】、；‘’，。、]+', u'', text)

    text = text.encode('utf-8')
    test_data = v.fit_transform([text])
    pred = clf.predict(test_data)
    return pred[0][0]


if __name__ == '__main__':
    r_dict = { 
         '0': u'汽车',
         '1': u'财经',
         '2': u'科技',
         '3': u'健康',
         '4': u'体育',
    }

    r = calssify('''
        
        网易科技讯 4月28日消息，苹果（NASDAQ: AAPL）当日公布了截至3月28日2015财年第二财季财报。报告显示，苹果该季度营收580亿美元，去年同期为456亿美元，同比增长27%；净利润136亿美元，去年同期为102亿美元，同比增长34%；合摊薄后每股收益2.33美元，去年同期为1.66美元，同比增长40%。

第二财季毛利率为40.8%，去年同期为39.3%。国际销售占到该季度总营收的69%。

本财季的增长主要源自iPhone和Mac电脑销售额均创下了第二财季记录，同时App Store的销售创下了历史记录。

“我们对于iPhone、Mac以及App Store体现出的持续的强劲势头感到惊讶，这也成为了我们创下历史最好第二财季财报数据的根本原因。”苹果首席执行官蒂姆·库克（Tim Cook）表示，“我们看到越来越多的人换成iPhone，这要多与此前任何一次升级周期。在本财季，Apple Watch的发布也有着一个强势的开始，我们为截至6月的季度而感到兴奋。”

“市场对我们产品和服务异常强劲的需求让我们在截至3月份的季度里实现了同比27%的营收增幅，和同比40%的每股收益增长。”苹果首席财务官卢卡·梅斯特里（Luca Maestri）表示，“该季度我们来自运营的现金流达到了191亿美元。”

苹果当前对2015财年第三财季作出如下预期：

·营收将在460亿美元至480亿美元之间

·毛利率将在38.5%至39.5%之间

·运营支出将在56.5亿至57.5亿美元之间

·其他收入为3.50亿美元

·有效税率为26.3%

营收按地区划分

·美洲地区营收为213.16亿美元，上季度为305.66亿美元，去年同期为179.82亿美元，环比下滑30%，同比增长19%；

·欧洲地区营收为122.04亿美元，上季度为172.14亿美元，去年同期为109.41亿美元，环比下滑29%，同比增长12%；

·大中华地区营收为168.23亿美元，上季度为161.44亿美元，去年同期为98.35亿美元，环比增长4%，同比增长71%；

·日本地区营收为34.57亿美元，上季度为54.48亿美元，去年同期为40.47亿美元，环比下滑37%，同比下滑15%；

·其他亚太地区营收为42.10亿美元，上季度为52.27亿美元，去年同期为28.41亿美元，环比下滑19%，同比增长48%；

营收按产品划分

·iPhone总销量为6117.0万部，营收为402.82亿美元；上季度销量为7446.8万部，营收为511.82亿美元；去年同期销量为4371.9万部，营收为260.64亿美元。销量环比下滑18%，同比增长40%；营收环比下滑21%，同比增长55%。

·iPad总销量为1262.3万台，营收为54.28亿美元；上季度销量为2141.9万台，营收为89.85亿美元；去年同期销量为1635.0万台，营收为76.10亿美元。销量环比下滑41%，同比下滑23%；营收环比下滑40%，同比下滑29%；


·Mac电脑总销量为456.3万台，营收为56.15亿美元；上季度销量为551.9万台，营收为69.44亿美元；去年同期销量为413.6万台，营收为55.19亿美元。销量环比下滑17%，同比增长10%；营收环比下滑19%，同比增长2%；

·iTunes、App Store、Apple Pay以及其它服务营收为49.96亿美元，上季度为47.99亿美元，去年同期为45.73亿美元，环比增长4%，同比增长9%；

·外围设备及其它硬件营收为16.89亿美元，上季度为26.89亿美元，去年同期为18.80亿美元，环比下滑37%，同比下滑10%。（卢鑫）

    ''')
    print(r, r_dict[r])
