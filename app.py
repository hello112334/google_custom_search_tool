import requests
import pandas as pd
import difflib

# APIキーとCustom Search EngineのID
api_key = "YOUR_API_KEY"
cx = "YOUR_SEARCH_ENGINE_ID"

def google_custom_search(query, api_key, cx):
    """note"""
    url = "https://www.googleapis.com/customsearch/v1"
    # url =  "https://www.googleapis.com/customsearch/v1/siterestrict"

    params = {'key': api_key, 'cx': cx, 'q': query}
    response = requests.get(url, params=params)

    return response.json()

def get_valid_webpage_link(search_results, query):
    """note"""
    for item in search_results.get('items', []):
        title = item['title']
        link = item['link']

        # 類似度の計算
        similarity = difflib.SequenceMatcher(None, query, title).ratio()

        # 類似度が60%以上かつPDFやExcel、WordファイルのURLを除外
        if similarity >= 0.0 and not link.endswith(('.pdf', '.xls', '.xlsx', '.doc', '.docx')):
            return link
    return "-"

if __name__ == '__main__':

    # 'support_organizations.csv' から支援機構のリストを読み込む
    df_organizations = pd.read_csv('support_organizations.csv', encoding='shift_jis')
    support_organizations = df_organizations['name'].tolist()

    # 'list.csv' から都道府県と市町村を読み込む
    df_list = pd.read_csv('list.csv', encoding='shift_jis')

    # 結果を保存するための空のDataFrameを作成
    df_results = pd.DataFrame(columns=["city", "town"] + support_organizations)

    # 検索クエリを生成し、検索を実行
    for index, row in df_list.iterrows():
        results_row = [row['city'], row['town']]
        print(f"[INFO][{index}] CHECK:{row['city']} {row['town']}")

        for organization in support_organizations:
            try:
                # print(f"[INFO][{index}] {organization}")
                query = f"{row['city']} {row['town']} {organization}"
                # print(f"[INFO][{index}] {query}")

                search_results = google_custom_search(query, api_key, cx)
                link = get_valid_webpage_link(search_results, query)
                # print(f"[INFO][{index}] {link}")

                results_row.append(link)

            except Exception as e:
                print(f"[ERROR][{index}] {e}")
                results_row.append("-")

        df_results.loc[len(df_results)] = results_row

    # 結果をCSVに保存
    df_results.to_csv("google_search_results.csv", index=False)
