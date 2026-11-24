# LION LEAD 導領 APP 流程模擬器

雄獅旅遊 導領平台（iPad 領隊 APP）之「出團前 → 帶團中」可點擊靜態原型 / 流程模擬器，供同仁與 IT 展示討論。

線上版（發佈後填入 Render 網址）：`https://<your-service>.onrender.com`

## 內容結構

- `scratch/sim_shell.html` — 模擬器外殼與狀態機（導覽、交班流程、各彈窗）
- `scratch/gen_pretour.py` — 產生各畫面（出團前 / 回團後 / 分房表 / 團體大表…）
- `scratch/convert.py` — 組裝所有畫面成單一 `sim/index.html`
- `project/*.dc.html` — 各靜態畫面原稿
- `assets/` — logo、啟動圖等素材
- `sim/index.html` — **已編譯好的成品**（Render 直接發佈這個資料夾）

## 本機重新編譯

```bash
python3 scratch/gen_pretour.py
python3 scratch/convert.py
# 產出：sim/index.html
```

本機預覽：用瀏覽器開啟 `sim/index.html` 即可。

## 部署到 Render（靜態網站）

1. 將本專案推上 GitHub。
2. 到 Render → New → **Static Site**，連結此 GitHub repo。
3. 設定：
   - **Build Command**：留空（已內建編譯好的 `sim/`）
   - **Publish Directory**：`sim`
4. Create Static Site，等待部署完成，即可取得 `https://<service>.onrender.com`。

> 本 repo 已附 `render.yaml`，若用 Render Blueprint（New → Blueprint）連結 repo，會自動套用上述設定。

日後若修改畫面：重新執行上面的編譯指令、commit `sim/index.html` 後 push，Render 會自動重新部署。
