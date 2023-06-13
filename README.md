# 100 Days of Python

## Day 1

### 閱讀文章
- [01.初识Python.md](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/01.初识Python.md)
- [學了 Python 能用來做什麼？| Medium](https://allaboutdataanalysis.medium.com/學了-python-能用來做什麼-3a5062113267)
- [Draw Rainbow using Turtle Graphics in Python - GeeksforGeeks](https://www.geeksforgeeks.org/draw-rainbow-using-turtle-graphics-in-python/)
- [4.8. A Few More turtle Methods and Observations — How to Think like a Computer Scientist: Interactive Edition](https://runestone.academy/ns/books/published/thinkcspy/PythonTurtle/AFewMoreturtleMethodsandObservations.html)

---

- Setup Github repository
- 設計人為吉多·范羅蘇姆（Guido van Rossum）
- 裝好了 Python 3.11
- 閱讀了 The Zen of Python （`import this`）
- Python 可以用來：
	- 網站後端
	- 自動化運維
	- DevOps
	- 爬蟲
	- 資料分析
	- 人工智慧
- 簡單小烏龜畫星星
![turtle.png](day1/turtle.png)

## Day 2

### 閱讀文章
- [02.语言元素.md](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/02.语言元素.md)
- [03.分支结构.md](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/03.分支结构.md)
- [04.循环结构.md](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/04.循环结构.md)
- [05.构造程序逻辑.md](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/05.构造程序逻辑.md)
- [06.函数和模块的使用.md](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/06.函数和模块的使用.md)

### 小練習
- Piece of Cake! | Kattis
- Cut the Negativity | Kattis

---

- 變數命名使用下底線分隔
- 轉換變數型態
	- `int()`
	- `float()`
	- `str()`
	- `chr()`
	- `ord()`
- 使用 `input()` 擷取輸入
- 格式化輸出 `print('%d + %d = %d' % (a, b, a + b))`
- 格式化輸出 `print(f'{f:.1f}華氏度 = {c:.1f}攝氏度')`
- 可以用反斜線拆行
  ```Python
  is_leap = year % 4 == 0 and year % 100 != 0 or \
          year % 400 == 0
	```
- 預設參數值
  ```Python
  def roll_dice(n=2):
    total = 0
    for i in range(n):
        total += randint(1, 6)
    return total
	```
- 不固定參數數量
  ```Python
  def sum(*args):
    total = 0
    for val in args:
        total += val
    return total
	```
- Main function
  ```Python
  if __name__ == '__main__':
	  print('Hello, world!')
	```