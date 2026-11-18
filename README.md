# 本土化产品市场概览

产品配方批次、用户反馈和市场订单。当前总览只按市场统计销售件数。

样例数据均为本地合成记录，不对应真实个人、媒体、机构或交易。项目使用 Python 3.11.2 标准库，数据随项目保存，不访问外部服务。

## 使用

在项目根目录运行 `python3 -m app summary` 查看按当前基础口径生成的 JSON 总览。

## 验证

运行 `python3 -m unittest discover -s tests -v` 和 `python3 -m compileall -q app tests`。

## 结构

`data/data.json` 保存领域记录与基础汇总口径；`app/storage.py` 读取并检查数据形状；`app/analysis.py` 计算基础分组统计；`app/service.py` 组合数据读取和统计；`tests/` 验证产品入口及无效数据处理。

## 工作台

`python3 -m app catalog` 查询在售批次，`python3 -m app margin` 按渠道的现行市场归属汇总订单净贡献（已知退货成本已扣）；`python3 -m app budget` 扣除订好的投放后，按在售批次的净贡献推荐下一笔预算去向。

同一 `sku` 可能经历不同配方批次。`return_until` 是订单最后可退日（含当天）；未到期订单仍显示在当前账面净贡献。`spend` 是实际发生的活动支出，`commitments` 则区分已订投放与可改草案。金额均用分。

操作数据在 `data/workbench.json`。工作台涉及的领域代码：`markets` 判定当前销售归属和在售配方, `economics` 核成熟度前的净贡献, `planning` 生成下一轮预算建议。已有总览仍使用 `data/data.json`。
