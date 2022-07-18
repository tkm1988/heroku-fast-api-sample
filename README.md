# heroku-fast-api-sample

## 注意事項

### パッケージをpoetryに追加した場合に手動でrequirements.txtを作成する

Herokuはpoetryをサポートしておらず、Buildではpip installするのみである。そのため、poetryによるパッケージ管理とは別にHerokuでサーバを動かすためにrequirements.txtを作成しなければならない。
npmのようなタスクランナーもPythonにはないためビルド前処理をフックして入れることもできない。そのため、パッケージに何か追加したものがある場合、手動で以下のコマンドを実行してPRに含めねばならない。

```sh
poetry export -f requirements.txt --output requirements.txt  
```

## 参考文献

<https://github.com/nsidnev/fastapi-realworld-example-app>
