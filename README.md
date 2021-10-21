# Github auto grass grower

## 使用方法

### Step1

[このページ](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)にしたがってGithubのaccess tokenを取り出す。

### Step2

以下のコマンドでイメージをPullする。
```shell
$ docker pull kuroicc/github-auto-grass-grower
```

### Step3

以下のようなコマンドを実行すると動きます。例にある五つの環境変数は必要変数です。
```shell
docker run -it \
-e TZ="Asia/Tokyo" \
-e GITHUB_USERNAME=Your Github Username \
-e GITHUB_TOKEN=Your Access Token \
-e repo_url=Your Repository URL \
-e email=Your Github Email \
--name github-auto-grass-grower \
kuroicc/github-auto-grass-grower
```
