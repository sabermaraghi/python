import asyncio


async  def t1():
    await t2()
    print('t1')
async def t2():
    await t3()
    print('t2')
async def t3():
    print('t3')

asyncio.run(t1())
