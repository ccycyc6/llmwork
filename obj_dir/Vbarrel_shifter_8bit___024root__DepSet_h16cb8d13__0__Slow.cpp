// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vbarrel_shifter_8bit.h for the primary calling header

#include "Vbarrel_shifter_8bit__pch.h"
#include "Vbarrel_shifter_8bit__Syms.h"
#include "Vbarrel_shifter_8bit___024root.h"

#ifdef VL_DEBUG
VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___dump_triggers__stl(Vbarrel_shifter_8bit___024root* vlSelf);
#endif  // VL_DEBUG

VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___eval_triggers__stl(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___eval_triggers__stl\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.__VstlTriggered.setBit(0U, (IData)(vlSelfRef.__VstlFirstIteration));
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        Vbarrel_shifter_8bit___024root___dump_triggers__stl(vlSelf);
    }
#endif
}
