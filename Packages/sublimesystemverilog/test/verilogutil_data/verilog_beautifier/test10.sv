wire a = b;
wire aaa = bbbb & dddd;
wire aaaaa = bbbbbbbbbbb;
wire a [0] = b[0];
wire aaa[0] = bbbbb[0] | dddd[0];
wire aaaaa[0] = bbbbbbbbbbb[0];
wire [1:3] a = b [1:4];
wire [1:3] aaa = bbbb[1:3]&dddd[1:3];
wire [1:3] a [2] = b [1:4][2];
wire [1:3] aaa[2] = bbbb[1:3][2]&dddd[1:3][2];

assign a = b;
assign aaa = bbbb & dddd;
assign aaaaa = bbbbbbbbbbb;
assign a [0] = b[0];
assign aaa[0] = bbbbb[0] | dddd[0];
assign aaaaa[0] = bbbbbbbbbbb[0];
assign [1:3] a = b [1:4];
assign [1:3] aaa = bbbb[1:3]&dddd[1:3];
assign [1:3] a [2] = b [1:4][2];
assign [1:3] aaa[2] = bbbb[1:3][2]&dddd[1:3][2];