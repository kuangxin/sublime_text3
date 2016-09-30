import sublime, sublime_plugin
import datetime, getpass
class ModuleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("insert_snippet",{"contents":"%s" % 
'''//----------------------------------------------------NUST-----------------------------------------------------
// ==============================420=================================
// Project Name :   
// File name    :   $1.v
// Library      :   WORK
// Created On   :   '''+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %a")+'''
// Comments     :   
// ----------------------------------------------------------------------
// Revision History :
// ----------------------------------------------------------------------
//  Ver :           | Author:   kuangxin    | Mod. Date :    |    
//  Update Detail:                  | 
// ----------------------------------------------------------------------
// OverView
// ========
//
// ----------------------------------------------------------------------
// ======================================================================
`timescale 1ns/100ps
module  $1(
    input I_rst_n    ,
    input I_sys_clk  ,
    output reg O_data
    );

//-----------------------------------------Internal Reg Definitions----------------------------------------------

//====parameter====
parameter       TCO_DELAY       =  1;

//====internal wire define====
wire[13:0]      W_                  ;
wire[13:0]      W_                  ;

//====internal register define====
reg[13:0]       R_                  ;
reg[13:0]       R1_                 ;

//---------------------------------------------Main Body of Code-------------------------------------------------
//=====================read me=====================
//
//  
//  
//  
//
//
//=====================read me=====================

always_ff @(posedge I_sys_clk or negedge I_rst_n) begin
    if(~I_rst_n) begin
        R_count <= 0;
    end else begin
        R_count <= ;
    end
end

//-------------------------------------output-------------------------------------
assign  O_signal_I_dat  =   W_hw_i_result;
assign  O_signal_Q_dat  =   W_hw_q_result;

//-------------------------------------output-------------------------------------
endmodule
//====END===='''
})

