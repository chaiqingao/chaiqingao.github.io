---
title: 1003 Emergency (25分)
date: 2020-04-27 19:07:26
updated: 2020-05-26 23:31:18
mathjax: true
tags:
- CPP
- 算法
- Dijkstra
- 最短路径
categories:
- [PAT甲级真题]
- [图算法]
---
As an emergency rescue team leader of a city, you are given a special map of your country. The map shows several scattered cities connected by some roads. Amount of rescue teams in each city and the length of each road between any pair of cities are marked on the map. When there is an emergency call to you from some other city, your job is to lead your men to the place as quickly as possible, and at the mean time, call up as many hands on the way as possible.

<!--more-->

## Input Specification

Each input file contains one test case. For each test case, the first line contains 4 positive integers: $N (≤500)$ - the number of cities (and the cities are numbered from $0$ to $N−1$), $M$ - the number of roads, $C_1$ and $C_2$ - the cities that you are currently in and that you must save, respectively. The next line contains $N$ integers, where the $i$-th integer is the number of rescue teams in the $i$-th city. Then $M$ lines follow, each describes a road with three integers $c_1$, $c_​2$ and $L$, which are the pair of cities connected by a road and the length of that road, respectively. It is guaranteed that there exists at least one path from $C_1$ to $C_2$.

## Output Specification

For each test case, print in one line two numbers: the number of different shortest paths between $C_1$ and $C_2$, and the maximum amount of rescue teams you can possibly gather. All the numbers in a line must be separated by exactly one space, and there is no extra space allowed at the end of a line.

## Sample Input

```bash
5 6 0 2
1 2 1 5 3
0 1 1
0 2 2
0 3 1
1 2 1
2 4 1
3 4 1
```

## Sample Output

```bash
2 4
```

## 分析

题目大意为：现给定一张无向图（节点有权），求从一点出发到另一点的最短路径的条数，以及经过节点的权之和的最大值。

利用Dijkstra算法，求起点到其余点的最短路径。（1）求最短路径条数：为每个节点分配一个num表示最短路径条数，在找到最近点v更新其余点时，若以最近点v为中转点u与s距离更近则`num[u]=num[v]`；若距离相等，则说明有多条路径，即`num[u]+=num[v]`。（2）求经过节点的权之和的最大值：为每个节点分配一个w表示权重之和（weight为该节点权重），在找到最近点v更新其余点时，若以最近点v为中转点u与s距离更近，则`w[u]=weight[u]+w[v]`；若距离相等，则需要判断哪条路径权重之和更大，`w[u]=max(w[u],weight[u]+w[u])`。

## AC代码

```cpp
#include &lt;iostream&gt;
using namespace std;
#define MAXV 500
const int INF = 0x3fffffff;
int dis[MAXV][MAXV], d[MAXV], num[MAXV] = { 0 }, weight[MAXV], w[MAXV] = { 0 };
bool vis[MAXV] = { false };
int n, m, st, ed;
void dijkstra(int s)
{
    fill(d, d + MAXV, INF);
    d[s] = 0;
    w[s] = weight[s];
    num[s] = 1;
    for (int i = 0; i &lt; n; i++)
    {
        int v = -1, mindis = INF;
        for (int j = 0; j &lt; n; j++)
        {
            if (!vis[j] && d[j] &lt; mindis)
            {
                mindis = d[j];
                v = j;
            }
        }
        if (v == -1 || v == ed) return;
        vis[v] = true;
        for (int j = 0; j &lt; n; j++)
        {
            if (!vis[j] && dis[v][j] != INF)
            {
                if (d[v] + dis[v][j] &lt; d[j])
                {
                    d[j] = d[v] + dis[v][j];
                    num[j] = num[v];
                    w[j] = weight[j] + w[v];
                }
                else if (d[v] + dis[v][j] == d[j])
                {
                    num[j] += num[v];
                    if (weight[j] + w[v] &gt; w[j]) w[j] = weight[j] + w[v];
                }
            }
        }
    }
}
int main()
{
    fill(dis[0], dis[0] + MAXV * MAXV, INF);
    scanf("%d%d%d%d", &n, &m, &st, &ed);
    for (int i = 0; i < n; i++) scanf("%d", &weight[i]);
    for (int i = 0; i < m; i++)
    {
        int s, e, l;
        scanf("%d%d%d", &s, &e, &l);
        dis[s][e] = dis[e][s] = l;
    }
    dijkstra(st);
    printf("%d %d", num[ed], w[ed]);
    return 0;
}
```

## 原题地址

[1003 Emergency (25分)](https://pintia.cn/problem-sets/994805342720868352/problems/994805523835109376)
