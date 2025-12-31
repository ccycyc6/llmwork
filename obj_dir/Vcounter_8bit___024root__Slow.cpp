// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vcounter_8bit.h for the primary calling header

#include "Vcounter_8bit__pch.h"
#include "Vcounter_8bit__Syms.h"
#include "Vcounter_8bit___024root.h"

void Vcounter_8bit___024root___ctor_var_reset(Vcounter_8bit___024root* vlSelf);

Vcounter_8bit___024root::Vcounter_8bit___024root(Vcounter_8bit__Syms* symsp, const char* v__name)
    : VerilatedModule{v__name}
    , vlSymsp{symsp}
 {
    // Reset structure values
    Vcounter_8bit___024root___ctor_var_reset(this);
}

void Vcounter_8bit___024root::__Vconfigure(bool first) {
    (void)first;  // Prevent unused variable warning
}

Vcounter_8bit___024root::~Vcounter_8bit___024root() {
}
