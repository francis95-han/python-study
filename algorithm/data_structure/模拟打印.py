#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from pythonds.basic.queue import Queue

'''
如果是，则表示打印机正忙，需要的等待时间可以由当前任务的打印张数求得。同时初始构造函数还要能完成单位时间打印张数的初始化设置。方法 tick 用于减去内设任务的完成所需时间，并在一次任务结束后将打印机设为闲置'''


class Printer:  # 模拟打印机
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def setStart(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * 60 / self.pagerate


'''
当一个任务被创建时，随机数生成器产生一个 1 到 20之间的一个随机数代表需打印的页数。我们选择调用 random 模块中的 randrange 方法。每个打印任务还需要定义一个用于计算等待时间的对象 timestamp。 timestamp 会记录下任务被创建和被放入打印队列时的时间。方法 waitTime 用于检索任务开始打印前在队列中的等待时长。'''


class Task:  # 模拟打印队任务
    def __init__(self, time):
        self.timestamp = time
        self.page = random.randrange(1, 12)

    def getPages(self):
        return self.page

    def getStamp(self):
        return self.timestamp

    def waitTime(self, currentTime):
        return currentTime - self.timestamp


'''
对象 printQueue 是我们现有的抽象数据类型队列的一个实例。我们借助布尔数学体系的方法 newPrintTask 决定是否生成新的打印任务。同时我们再一次调用 random 模块中的 randrange 函数来得到一个 1 到 180 之间的随机整数(32 行)，据此模拟这个随机事件。模拟函数让我们可以为打印机设置总时长和单位时间打印张数'''


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.setStart(nexttask)
        labprinter.tick()
    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))


def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 5)
