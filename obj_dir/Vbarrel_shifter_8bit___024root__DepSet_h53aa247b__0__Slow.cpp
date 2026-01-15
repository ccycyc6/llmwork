// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vbarrel_shifter_8bit.h for the primary calling header

#include "Vbarrel_shifter_8bit__pch.h"
#include "Vbarrel_shifter_8bit___024root.h"

VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___eval_static(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___eval_static\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
}

VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___eval_initial(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___eval_initial\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
}

VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___eval_final(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___eval_final\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___dump_triggers__stl(Vbarrel_shifter_8bit___024root* vlSelf);
#endif  // VL_DEBUG
VL_ATTR_COLD bool Vbarrel_shifter_8bit___024root___eval_phase__stl(Vbarrel_shifter_8bit___024root* vlSelf);

VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___eval_settle(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___eval_settle\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Init
    IData/*31:0*/ __VstlIterCount;
    CData/*0:0*/ __VstlContinue;
    // Body
    __VstlIterCount = 0U;
    vlSelfRef.__VstlFirstIteration = 1U;
    __VstlContinue = 1U;
    while (__VstlContinue) {
        if (VL_UNLIKELY(((0x64U < __VstlIterCount)))) {
#ifdef VL_DEBUG
            Vbarrel_shifter_8bit___024root___dump_triggers__stl(vlSelf);
#endif
            VL_FATAL_MT("666.v", 1, "", "Settle region did not converge.");
        }
        __VstlIterCount = ((IData)(1U) + __VstlIterCount);
        __VstlContinue = 0U;
        if (Vbarrel_shifter_8bit___024root___eval_phase__stl(vlSelf)) {
            __VstlContinue = 1U;
        }
        vlSelfRef.__VstlFirstIteration = 0U;
    }
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___dump_triggers__stl(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___dump_triggers__stl\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1U & (~ vlSelfRef.__VstlTriggered.any()))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
    if ((1ULL & vlSelfRef.__VstlTriggered.word(0U))) {
        VL_DBG_MSGF("         'stl' region trigger index 0 is active: Internal 'stl' trigger - first iteration\n");
    }
}
#endif  // VL_DEBUG

void Vbarrel_shifter_8bit___024root___ico_sequent__TOP__0(Vbarrel_shifter_8bit___024root* vlSelf);

VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___eval_stl(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___eval_stl\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1ULL & vlSelfRef.__VstlTriggered.word(0U))) {
        Vbarrel_shifter_8bit___024root___ico_sequent__TOP__0(vlSelf);
    }
}

VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___eval_triggers__stl(Vbarrel_shifter_8bit___024root* vlSelf);

VL_ATTR_COLD bool Vbarrel_shifter_8bit___024root___eval_phase__stl(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___eval_phase__stl\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Init
    CData/*0:0*/ __VstlExecute;
    // Body
    Vbarrel_shifter_8bit___024root___eval_triggers__stl(vlSelf);
    __VstlExecute = vlSelfRef.__VstlTriggered.any();
    if (__VstlExecute) {
        Vbarrel_shifter_8bit___024root___eval_stl(vlSelf);
    }
    return (__VstlExecute);
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___dump_triggers__ico(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___dump_triggers__ico\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1U & (~ vlSelfRef.__VicoTriggered.any()))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
    if ((1ULL & vlSelfRef.__VicoTriggered.word(0U))) {
        VL_DBG_MSGF("         'ico' region trigger index 0 is active: Internal 'ico' trigger - first iteration\n");
    }
}
#endif  // VL_DEBUG

#ifdef VL_DEBUG
VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___dump_triggers__act(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___dump_triggers__act\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1U & (~ vlSelfRef.__VactTriggered.any()))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
}
#endif  // VL_DEBUG

#ifdef VL_DEBUG
VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___dump_triggers__nba(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___dump_triggers__nba\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1U & (~ vlSelfRef.__VnbaTriggered.any()))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
}
#endif  // VL_DEBUG

VL_ATTR_COLD void Vbarrel_shifter_8bit___024root___ctor_var_reset(Vbarrel_shifter_8bit___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root___ctor_var_reset\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    const uint64_t __VscopeHash = VL_MURMUR64_HASH(vlSelf->name());
    vlSelf->data_in = VL_SCOPED_RAND_RESET_I(8, __VscopeHash, 10574596302020702150ull);
    vlSelf->shift_amount = VL_SCOPED_RAND_RESET_I(3, __VscopeHash, 3167575699312874446ull);
    vlSelf->shift_direction = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 787222672351837558ull);
    vlSelf->data_out = VL_SCOPED_RAND_RESET_I(8, __VscopeHash, 11675680895196038875ull);
}
