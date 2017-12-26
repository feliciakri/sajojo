cmd_arch/arm/boot/dts/bcm2835-rpi-zero.dtb := mkdir -p arch/arm/boot/dts/ ; /home/valen/raspberry-linux/tools/arm-bcm2708/arm-bcm2708-linux-gnueabi/bin/arm-bcm2708-linux-gnueabi-gcc -E -Wp,-MD,arch/arm/boot/dts/.bcm2835-rpi-zero.dtb.d.pre.tmp -nostdinc -I./arch/arm/boot/dts -I./arch/arm/boot/dts/include -I./drivers/of/testcase-data -undef -D__DTS__ -x assembler-with-cpp -o arch/arm/boot/dts/.bcm2835-rpi-zero.dtb.dts.tmp arch/arm/boot/dts/bcm2835-rpi-zero.dts ; ./scripts/dtc/dtc -O dtb -o arch/arm/boot/dts/bcm2835-rpi-zero.dtb -b 0 -i arch/arm/boot/dts/ -@ -H epapr -Wno-unit_address_vs_reg -d arch/arm/boot/dts/.bcm2835-rpi-zero.dtb.d.dtc.tmp arch/arm/boot/dts/.bcm2835-rpi-zero.dtb.dts.tmp ; cat arch/arm/boot/dts/.bcm2835-rpi-zero.dtb.d.pre.tmp arch/arm/boot/dts/.bcm2835-rpi-zero.dtb.d.dtc.tmp > arch/arm/boot/dts/.bcm2835-rpi-zero.dtb.d

source_arch/arm/boot/dts/bcm2835-rpi-zero.dtb := arch/arm/boot/dts/bcm2835-rpi-zero.dts

deps_arch/arm/boot/dts/bcm2835-rpi-zero.dtb := \
  arch/arm/boot/dts/bcm2835.dtsi \
  arch/arm/boot/dts/bcm283x.dtsi \
  arch/arm/boot/dts/include/dt-bindings/pinctrl/bcm2835.h \
  arch/arm/boot/dts/include/dt-bindings/clock/bcm2835.h \
  arch/arm/boot/dts/include/dt-bindings/clock/bcm2835-aux.h \
  arch/arm/boot/dts/include/dt-bindings/gpio/gpio.h \
  arch/arm/boot/dts/bcm2835-rpi.dtsi \
  arch/arm/boot/dts/include/dt-bindings/power/raspberrypi-power.h \
  arch/arm/boot/dts/bcm283x-rpi-usb-host.dtsi \

arch/arm/boot/dts/bcm2835-rpi-zero.dtb: $(deps_arch/arm/boot/dts/bcm2835-rpi-zero.dtb)

$(deps_arch/arm/boot/dts/bcm2835-rpi-zero.dtb):
