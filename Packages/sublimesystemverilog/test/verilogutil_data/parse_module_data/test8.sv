module a();

 parameter a1 = 1_000,
	a2 = a1*3,
	a3 = a1*a2,
	a4 = a2-a1,
	a5 = a1+a2,
	a6 = (a1+a2)*2,
	a7 = (a1+a2)+a3,
	a8 = a2/a1,
	a9 = a2 >>> 1,
	a10 = a2 <<< a1;

 parameter int a11 = 8'h4A, a12 = 54;


endmodule