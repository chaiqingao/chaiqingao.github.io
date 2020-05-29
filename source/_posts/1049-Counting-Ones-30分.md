---
title: 1049 Counting Ones (30分)
date: 2020-05-29 10:28:39
updated: 2020-05-29 10:28:39
mathjax: true
tags:
- CPP
- 算法
- 数学问题
categories:
- PAT甲级真题
---

The task is simple: given any positive integer $N$, you are supposed to count the total number of 1's in the decimal form of the integers from 1 to $N$. For example, given $N$ being 12, there are five 1's in 1, 10, 11, and 12.

<!--more-->

## Input Specification

Each input file contains one test case which gives the positive $N$ ($\le 2^{30}$).

## Output Specification

For each test case, print the number of 1's in one line.

## Sample Input

```in
12
```

## Sample Output

```out
5
```

## 分析

题目大意为：给定一个数字$N$，统计从1到$N$中所有数字里1出现的次数。

以数字`abcdef`为例遍历每一位，统计该位取1时的数字个数，以`d`为例

- 若$d=0$，左侧可取$[0,abc)$，右侧可取$[0, 99]$，共$abc*10^2$个
- 若$d>1$，左侧可取$[0, abc]$，右侧可取$[0, 99]$，共$(abc+1)*10^2$个
- 若$d=1$，左侧取$[0,abc)$时右侧可取$[0, 99]$，左侧取$abc$时，右侧可取$[0, ef]$，共$abc*10^2+ef+1$个

将每一位的个数求和即可得到结果

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <string>
using namespace std;
int to(string s)
{
    int res = 0;
    for (int i = 0; i < s.size(); i++) res = res * 10 + s[i] - '0';
    return res;
}
int main()
{
    char n[15]; scanf("%s", n);
    int len = strlen(n);
    int res = 0;
    for (int i = len - 1, k = 1; i >= 0; i--, k *= 10)
    {
        res += to(string(n, i)) * k;
        if (n[i] > '1') res += k;
        else if (n[i] == '1') res += to(string(n, i + 1, len)) + 1;
    }
    printf("%d", res);
    return 0;
}
```

## 原题地址

[1049 Counting Ones (30分)](https://pintia.cn/problem-sets/994805342720868352/problems/994805430595731456)
