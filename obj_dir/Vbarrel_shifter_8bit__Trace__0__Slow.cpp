// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Tracing implementation internals
#include "verilated_fst_c.h"
#include "Vbarrel_shifter_8bit__Syms.h"


VL_ATTR_COLD void Vbarrel_shifter_8bit___024root__trace_init_sub__TOP__0(Vbarrel_shifter_8bit___024root* vlSelf, VerilatedFst* tracep) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root__trace_init_sub__TOP__0\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Init
    const int c = vlSymsp->__Vm_baseCode;
    // Body
    tracep->pushPrefix("$rootio", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBus(c+1,0,"data_in",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 7,0);
    tracep->declBus(c+2,0,"shift_amount",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 2,0);
    tracep->declBit(c+3,0,"shift_direction",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBus(c+4,0,"data_out",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 7,0);
    tracep->popPrefix();
    tracep->pushPrefix("barrel_shifter_8bit", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBus(c+1,0,"data_in",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 7,0);
    tracep->declBus(c+2,0,"shift_amount",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 2,0);
    tracep->declBit(c+3,0,"shift_direction",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBus(c+4,0,"data_out",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 7,0);
    tracep->popPrefix();
}

VL_ATTR_COLD void Vbarrel_shifter_8bit___024root__trace_init_top(Vbarrel_shifter_8bit___024root* vlSelf, VerilatedFst* tracep) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root__trace_init_top\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    Vbarrel_shifter_8bit___024root__trace_init_sub__TOP__0(vlSelf, tracep);
}

VL_ATTR_COLD void Vbarrel_shifter_8bit___024root__trace_const_0(void* voidSelf, VerilatedFst::Buffer* bufp);
VL_ATTR_COLD void Vbarrel_shifter_8bit___024root__trace_full_0(void* voidSelf, VerilatedFst::Buffer* bufp);
void Vbarrel_shifter_8bit___024root__trace_chg_0(void* voidSelf, VerilatedFst::Buffer* bufp);
void Vbarrel_shifter_8bit___024root__trace_cleanup(void* voidSelf, VerilatedFst* /*unused*/);

VL_ATTR_COLD void Vbarrel_shifter_8bit___024root__trace_register(Vbarrel_shifter_8bit___024root* vlSelf, VerilatedFst* tracep) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root__trace_register\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    tracep->addConstCb(&Vbarrel_shifter_8bit___024root__trace_const_0, 0U, vlSelf);
    tracep->addFullCb(&Vbarrel_shifter_8bit___024root__trace_full_0, 0U, vlSelf);
    tracep->addChgCb(&Vbarrel_shifter_8bit___024root__trace_chg_0, 0U, vlSelf);
    tracep->addCleanupCb(&Vbarrel_shifter_8bit___024root__trace_cleanup, vlSelf);
}

VL_ATTR_COLD void Vbarrel_shifter_8bit___024root__trace_const_0(void* voidSelf, VerilatedFst::Buffer* bufp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root__trace_const_0\n"); );
    // Init
    Vbarrel_shifter_8bit___024root* const __restrict vlSelf VL_ATTR_UNUSED = static_cast<Vbarrel_shifter_8bit___024root*>(voidSelf);
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
}

VL_ATTR_COLD void Vbarrel_shifter_8bit___024root__trace_full_0_sub_0(Vbarrel_shifter_8bit___024root* vlSelf, VerilatedFst::Buffer* bufp);

VL_ATTR_COLD void Vbarrel_shifter_8bit___024root__trace_full_0(void* voidSelf, VerilatedFst::Buffer* bufp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root__trace_full_0\n"); );
    // Init
    Vbarrel_shifter_8bit___024root* const __restrict vlSelf VL_ATTR_UNUSED = static_cast<Vbarrel_shifter_8bit___024root*>(voidSelf);
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    // Body
    Vbarrel_shifter_8bit___024root__trace_full_0_sub_0((&vlSymsp->TOP), bufp);
}

VL_ATTR_COLD void Vbarrel_shifter_8bit___024root__trace_full_0_sub_0(Vbarrel_shifter_8bit___024root* vlSelf, VerilatedFst::Buffer* bufp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vbarrel_shifter_8bit___024root__trace_full_0_sub_0\n"); );
    Vbarrel_shifter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Init
    uint32_t* const oldp VL_ATTR_UNUSED = bufp->oldp(vlSymsp->__Vm_baseCode);
    // Body
    bufp->fullCData(oldp+1,(vlSelfRef.data_in),8);
    bufp->fullCData(oldp+2,(vlSelfRef.shift_amount),3);
    bufp->fullBit(oldp+3,(vlSelfRef.shift_direction));
    bufp->fullCData(oldp+4,(vlSelfRef.data_out),8);
}
