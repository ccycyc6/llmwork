// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Model implementation (design independent parts)

#include "Vcounter_8bit__pch.h"
#include "verilated_fst_c.h"

//============================================================
// Constructors

Vcounter_8bit::Vcounter_8bit(VerilatedContext* _vcontextp__, const char* _vcname__)
    : VerilatedModel{*_vcontextp__}
    , vlSymsp{new Vcounter_8bit__Syms(contextp(), _vcname__, this)}
    , clk{vlSymsp->TOP.clk}
    , rst_n{vlSymsp->TOP.rst_n}
    , en{vlSymsp->TOP.en}
    , count{vlSymsp->TOP.count}
    , rootp{&(vlSymsp->TOP)}
{
    // Register model with the context
    contextp()->addModel(this);
    contextp()->traceBaseModelCbAdd(
        [this](VerilatedTraceBaseC* tfp, int levels, int options) { traceBaseModel(tfp, levels, options); });
}

Vcounter_8bit::Vcounter_8bit(const char* _vcname__)
    : Vcounter_8bit(Verilated::threadContextp(), _vcname__)
{
}

//============================================================
// Destructor

Vcounter_8bit::~Vcounter_8bit() {
    delete vlSymsp;
}

//============================================================
// Evaluation function

#ifdef VL_DEBUG
void Vcounter_8bit___024root___eval_debug_assertions(Vcounter_8bit___024root* vlSelf);
#endif  // VL_DEBUG
void Vcounter_8bit___024root___eval_static(Vcounter_8bit___024root* vlSelf);
void Vcounter_8bit___024root___eval_initial(Vcounter_8bit___024root* vlSelf);
void Vcounter_8bit___024root___eval_settle(Vcounter_8bit___024root* vlSelf);
void Vcounter_8bit___024root___eval(Vcounter_8bit___024root* vlSelf);

void Vcounter_8bit::eval_step() {
    VL_DEBUG_IF(VL_DBG_MSGF("+++++TOP Evaluate Vcounter_8bit::eval_step\n"); );
#ifdef VL_DEBUG
    // Debug assertions
    Vcounter_8bit___024root___eval_debug_assertions(&(vlSymsp->TOP));
#endif  // VL_DEBUG
    vlSymsp->__Vm_activity = true;
    vlSymsp->__Vm_deleter.deleteAll();
    if (VL_UNLIKELY(!vlSymsp->__Vm_didInit)) {
        vlSymsp->__Vm_didInit = true;
        VL_DEBUG_IF(VL_DBG_MSGF("+ Initial\n"););
        Vcounter_8bit___024root___eval_static(&(vlSymsp->TOP));
        Vcounter_8bit___024root___eval_initial(&(vlSymsp->TOP));
        Vcounter_8bit___024root___eval_settle(&(vlSymsp->TOP));
    }
    VL_DEBUG_IF(VL_DBG_MSGF("+ Eval\n"););
    Vcounter_8bit___024root___eval(&(vlSymsp->TOP));
    // Evaluate cleanup
    Verilated::endOfEval(vlSymsp->__Vm_evalMsgQp);
}

//============================================================
// Events and timing
bool Vcounter_8bit::eventsPending() { return false; }

uint64_t Vcounter_8bit::nextTimeSlot() {
    VL_FATAL_MT(__FILE__, __LINE__, "", "No delays in the design");
    return 0;
}

//============================================================
// Utilities

const char* Vcounter_8bit::name() const {
    return vlSymsp->name();
}

//============================================================
// Invoke final blocks

void Vcounter_8bit___024root___eval_final(Vcounter_8bit___024root* vlSelf);

VL_ATTR_COLD void Vcounter_8bit::final() {
    Vcounter_8bit___024root___eval_final(&(vlSymsp->TOP));
}

//============================================================
// Implementations of abstract methods from VerilatedModel

const char* Vcounter_8bit::hierName() const { return vlSymsp->name(); }
const char* Vcounter_8bit::modelName() const { return "Vcounter_8bit"; }
unsigned Vcounter_8bit::threads() const { return 1; }
void Vcounter_8bit::prepareClone() const { contextp()->prepareClone(); }
void Vcounter_8bit::atClone() const {
    contextp()->threadPoolpOnClone();
}
std::unique_ptr<VerilatedTraceConfig> Vcounter_8bit::traceConfig() const {
    return std::unique_ptr<VerilatedTraceConfig>{new VerilatedTraceConfig{false, false, false}};
};

//============================================================
// Trace configuration

void Vcounter_8bit___024root__trace_decl_types(VerilatedFst* tracep);

void Vcounter_8bit___024root__trace_init_top(Vcounter_8bit___024root* vlSelf, VerilatedFst* tracep);

VL_ATTR_COLD static void trace_init(void* voidSelf, VerilatedFst* tracep, uint32_t code) {
    // Callback from tracep->open()
    Vcounter_8bit___024root* const __restrict vlSelf VL_ATTR_UNUSED = static_cast<Vcounter_8bit___024root*>(voidSelf);
    Vcounter_8bit__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    if (!vlSymsp->_vm_contextp__->calcUnusedSigs()) {
        VL_FATAL_MT(__FILE__, __LINE__, __FILE__,
            "Turning on wave traces requires Verilated::traceEverOn(true) call before time 0.");
    }
    vlSymsp->__Vm_baseCode = code;
    tracep->pushPrefix(std::string{vlSymsp->name()}, VerilatedTracePrefixType::SCOPE_MODULE);
    Vcounter_8bit___024root__trace_decl_types(tracep);
    Vcounter_8bit___024root__trace_init_top(vlSelf, tracep);
    tracep->popPrefix();
}

VL_ATTR_COLD void Vcounter_8bit___024root__trace_register(Vcounter_8bit___024root* vlSelf, VerilatedFst* tracep);

VL_ATTR_COLD void Vcounter_8bit::traceBaseModel(VerilatedTraceBaseC* tfp, int levels, int options) {
    (void)levels; (void)options;
    VerilatedFstC* const stfp = dynamic_cast<VerilatedFstC*>(tfp);
    if (VL_UNLIKELY(!stfp)) {
        vl_fatal(__FILE__, __LINE__, __FILE__,"'Vcounter_8bit::trace()' called on non-VerilatedFstC object;"
            " use --trace-fst with VerilatedFst object, and --trace-vcd with VerilatedVcd object");
    }
    stfp->spTrace()->addModel(this);
    stfp->spTrace()->addInitCb(&trace_init, &(vlSymsp->TOP));
    Vcounter_8bit___024root__trace_register(&(vlSymsp->TOP), stfp->spTrace());
}
