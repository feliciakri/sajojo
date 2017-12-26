cmd_arch/arm/boot/dts/overlays/hifiberry-digi.dtbo := mkdir -p arch/arm/boot/dts/overlays/ ; /home/valen/raspberry-linux/tools/arm-bcm2708/arm-bcm2708-linux-gnueabi/bin/arm-bcm2708-linux-gnueabi-gcc -E -Wp,-MD,arch/arm/boot/dts/overlays/.hifiberry-digi.dtbo.d.pre.tmp -nostdinc -I./arch/arm/boot/dts -I./arch/arm/boot/dts/include -I./drivers/of/testcase-data -undef -D__DTS__ -x assembler-with-cpp -o arch/arm/boot/dts/overlays/.hifiberry-digi.dtbo.dts.tmp arch/arm/boot/dts/overlays/hifiberry-digi-overlay.dts ; ./scripts/dtc/dtc -@ -H epapr -O dtb -o arch/arm/boot/dts/overlays/hifiberry-digi.dtbo -b 0 -i arch/arm/boot/dts/overlays/ -Wno-unit_address_vs_reg -d arch/arm/boot/dts/overlays/.hifiberry-digi.dtbo.d.dtc.tmp arch/arm/boot/dts/overlays/.hifiberry-digi.dtbo.dts.tmp ; cat arch/arm/boot/dts/overlays/.hifiberry-digi.dtbo.d.pre.tmp arch/arm/boot/dts/overlays/.hifiberry-digi.dtbo.d.dtc.tmp > arch/arm/boot/dts/overlays/.hifiberry-digi.dtbo.d

source_arch/arm/boot/dts/overlays/hifiberry-digi.dtbo := arch/arm/boot/dts/overlays/hifiberry-digi-overlay.dts

deps_arch/arm/boot/dts/overlays/hifiberry-digi.dtbo := \

arch/arm/boot/dts/overlays/hifiberry-digi.dtbo: $(deps_arch/arm/boot/dts/overlays/hifiberry-digi.dtbo)

$(deps_arch/arm/boot/dts/overlays/hifiberry-digi.dtbo):
