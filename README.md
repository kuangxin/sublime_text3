# sublime_text3 
sublime_text3 user config file\
## summary
This is a user config file special for using sublime_text3 to edit verilog file\
Thanks for the sublimesystemverilog package http://sv-doc.readthedocs.io/en/latest/ , it's an exellant plug-in for verilog with sublime and I do some modify to it.There are many useful funcions to help you improve efficiency.
## Reindentation
I modify the Reindentation style from this syle
```
always @(posedge I_sys_clk or posedge I_reset_p) begin
    if(I_reset_p) begin
        R_imag_dat[0] <= 0;
    end else begin
        R_imag_dat[0] <= I_imag_dat[8*1-1:0];
    end
end
```
to this style
```
always @(posedge I_sys_clk or posedge I_reset_p) 
begin
    if(I_reset_p)
    begin
        R_imag_dat[0] <= 0;
    end 
    else
    begin
        R_imag_dat[0] <= I_imag_dat[8*1-1:0];
    end
end
```
## Alignment
And I do some modify to alignment for align the port, such as
```
module pe (
    input             I_reset_p  ,
    input             I_sys_clk  ,
    input             I_imag_en  ,
    input      [63:0] I_imag_dat ,
    input             I_filt_en  ,
    input      [ 7:0] I_filt_dat ,
    output reg        O_imag_en  ,
    output reg [ 7:0] O_imag_dat
);
```
