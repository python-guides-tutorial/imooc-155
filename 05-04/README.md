# 5-4 unittest中case的管理及运用

|本期版本|上期版本
|:---:|:---:
`Sun Sep 24 00:05:23 CST 2023` | 

**跳过测试**

```python
@unittest.skip('test_02')
def test_02(self):
  pass
```

**手动测试**
```python
# unittest.main()

suite = unittest.TestSuite()
suite.addTest(TestUser('test_01'))
suite.addTest(TestUser('test_02'))
unittest.TextTestRunner().run(suite)
```