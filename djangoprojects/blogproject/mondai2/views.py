from django.shortcuts import render

# django.views.genericからListViewをインポート
from django.views.generic import ListView

# モデルMondai2Postをインポート
from .models import Mondai2Post

class StartView(ListView):
    '''トップページのビュー
    投稿記事を一覧表示するのでListViewを継承する
    Attributes:
      template_name: レンダリングするテンプレート
      context_object_name: object_listキーの別名を設定
      queryset: データベースのクエリ
    '''

    # index.htmlをレンダリングする
    template_name ='start.html'

    # object_listキーの別名を設定
    context_object_name = 'orderby_records'

    # モデルMondai2Postのオブジェクトにorder_by()を適用して
    # Mondai2Postのレコードを投稿日時の降順で並べ替える
    queryset = Mondai2Post.objects.order_by('-posted_at')