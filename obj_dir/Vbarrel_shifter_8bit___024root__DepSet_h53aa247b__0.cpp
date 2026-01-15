// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vbarrel_shifter_8bit.h for the primary calling header

#include "Vbarrel_shifter_8bit__pch.h"
#include "Vbarrel_shifter_8bit___024root.h"

void Vbarrel_shifter_8bit___024root___ico_sequent__TOP__0(Vbarrel_shifter_8bit___024root* vlSelf);

void Vbarrel_shifter_8bit___024root___eval_ico(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___eval_ico\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1ULL & vlSelfRef.__VicoTriggered.word(0U))) {
        Vbarrel_shifter_8bit___024root___ico_sequent__TOP__0(vlSelf);
    }
}

extern const VlUnpacked<CData/*7:0*/, 4096> Vbarrel_shifter_8bit__ConstPool__TABLE_h003eaf3f_0;

VL_INLINE_OPT void Vbarrel_shifter_8bit___024root___ico_sequent__TOP__0(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___ico_sequent__TOP__0\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Init
    SData/*11:0*/ __Vtableidx1;
    __Vtableidx1 = 0;
    // Body
    __Vtableidx1 = (((IData)(vlSelfRef.data_in) << 4U) 
                    | (((IData)(vlSelfRef.shift_amount) 
                        << 1U) | (IData)(vlSelfRef.shift_direction)));
    vlSelfRef.data_out = Vbarrel_shifter_8bit__ConstPool__TABLE_h003eaf3f_0
        [__Vtableidx1];
}

void Vbarrel_shifter_8bit___024root___eval_triggers__ico(Vbarrel_shifter_8bit___024root* vlSelf);

bool Vbarrel_shifter_8bit___024root___eval_phase__ico(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___eval_phase__ico\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Init
    CData/*0:0*/ __VicoExecute;
    // Body
    Vbarrel_shifter_8bit___024root___eval_triggers__ico(vlSelf);
    __VicoExecute = vlSelfRef.__VicoTriggered.any();
    if (__VicoExecute) {
        Vbarrel_shifter_8bit___024root___eval_ico(vlSelf);
    }
    return (__VicoExecute);
}

void Vbarrel_shifter_8bit___024root___eval_act(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___eval_act\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
}

void Vbarrel_shifter_8bit___024root___eval_nba(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___eval_nba\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
}

void Vbarrel_shifter_8bit___024root___eval_triggers__act(Vbarrel_shifter_8bit___024root* vlSelf);

bool Vbarrel_shifter_8bit___024root___eval_phase__act(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___eval_phase__act\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Init
    VlTriggerVec<0> __VpreTriggered;
    CData/*0:0*/ __VactExecute;
    // Body
    Vbarrel_shifter_8bit___024root___eval_triggers__act(vlSelf);
    __VactExecute = vlSelfRef.__VactTriggered.any();
    if (__VactExecute) {
        __VpreTriggered.andNot(vlSelfRef.__VactTriggered, vlSelfRef.__VnbaTriggered);
        vlSelfRef.__VnbaTriggered.thisOr(vlSelfRef.__VactTriggered);
        Vbarrel_shifter_8bit___024root___eval_act(vlSelf);
    }
    return (__VactExecute);
}

bool Vbarrel_shifter_8bit___024root___eval_phase__nba(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___eval_phase__nba\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Init
    CData/*0:0*/ __VnbaExecute;
    // Body
    __VnbaExecute = vlSelfRef.__VnbaTriggered.any();
    if (__VnbaExecute) {
        Vbarrel_shifter_8bit___024root___eval_nba(vlSelf);
        vlSelfRef.__VnbaTriggered.clear();
    }
    return (__VnbaExecute);
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___dump_triggers__ico(Vbarrel_shifter_8bit___024root* vlSelf);
#endif  // VL_DEBUG
#ifdef VL_DEBUG
VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___dump_triggers__nba(Vbarrel_shifter_8bit___024root* vlSelf);
#endif  // VL_DEBUG
#ifdef VL_DEBUG
VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___dump_triggers__act(Vbarrel_shifter_8bit___024root* vlSelf);
#endif  // VL_DEBUG

void Vbarrel_shifter_8bit___024root___eval(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___eval\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Init
    IData/*31:0*/ __VicoIterCount;
    CData/*0:0*/ __VicoContinue;
    IData/*31:0*/ __VnbaIterCount;
    CData/*0:0*/ __VnbaContinue;
    // Body
    __VicoIterCount = 0U;
    vlSelfRef.__VicoFirstIteration = 1U;
    __VicoContinue = 1U;
    while (__VicoContinue) {
        if (VL_UNLIKELY(((0x64U < __VicoIterCount)))) {
#ifdef VL_DEBUG
            Vbarrel_shifter_8bit___024root___dump_triggers__ico(vlSelf);
#endif
            VL_FATAL_MT("666.v", 1, "", "Input combinational region did not converge.");
        }
        __VicoIterCount = ((IData)(1U) + __VicoIterCount);
        __VicoContinue = 0U;
        if (Vbarrel_shifter_8bit___024root___eval_phase__ico(vlSelf)) {
            __VicoContinue = 1U;
        }
        vlSelfRef.__VicoFirstIteration = 0U;
    }
    __VnbaIterCount = 0U;
    __VnbaContinue = 1U;
    while (__VnbaContinue) {
        if (VL_UNLIKELY(((0x64U < __VnbaIterCount)))) {
#ifdef VL_DEBUG
            Vbarrel_shifter_8bit___024root___dump_triggers__nba(vlSelf);
#endif
            VL_FATAL_MT("666.v", 1, "", "NBA region did not converge.");
        }
        __VnbaIterCount = ((IData)(1U) + __VnbaIterCount);
        __VnbaContinue = 0U;
        vlSelfRef.__VactIterCount = 0U;
        vlSelfRef.__VactContinue = 1U;
        while (vlSelfRef.__VactContinue) {
            if (VL_UNLIKELY(((0x64U < vlSelfRef.__VactIterCount)))) {
#ifdef VL_DEBUG
                Vbarrel_shifter_8bit___024root___dump_triggers__act(vlSelf);
#endif
                VL_FATAL_MT("666.v", 1, "", "Active region did not converge.");
            }
            vlSelfRef.__VactIterCount = ((IData)(1U) 
                                         + vlSelfRef.__VactIterCount);
            vlSelfRef.__VactContinue = 0U;
            if (Vbarrel_shifter_8bit___024root___eval_phase__act(vlSelf)) {
                vlSelfRef.__VactContinue = 1U;
            }
        }
        if (Vbarrel_shifter_8bit___024root___eval_phase__nba(vlSelf)) {
            __VnbaContinue = 1U;
        }
    }
}

#ifdef VL_DEBUG
void Vbarrel_shifter_8bit___024root___eval_debug_assertions(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___eval_debug_assertions\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if (VL_UNLIKELY(((vlSelfRef.shift_amount & 0xf8U)))) {
        Verilated::overWidthError("shift_amount");}
    if (VL_UNLIKELY(((vlSelfRef.shift_direction & 0xfeU)))) {
        Verilated::overWidthError("shift_direction");}
}
#endif  // VL_DEBUG
