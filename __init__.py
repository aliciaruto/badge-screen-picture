import ugfx, badge

ugfx.init()
ugfx.LUT_FULL
ugfx.input_init()
ugfx.clear(ugfx.BLACK)
ugfx.flush()
ugfx.clear(ugfx.WHITE)
ugfx.flush()

def go_home(pushed):
    if(pushed):
        import machine
        machine.deepsleep(1)

ugfx.input_attach(ugfx.BTN_B, go_home)

badge.eink_png(100,50,'/lib/fiumerslogo/fiumers.png')
ugfx.flush()
