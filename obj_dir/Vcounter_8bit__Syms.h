// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Symbol table internal header
//
// Internal details; most calling programs do not need this header,
// unless using verilator public meta comments.

#ifndef VERILATED_VCOUNTER_8BIT__SYMS_H_
#define VERILATED_VCOUNTER_8BIT__SYMS_H_  // guard

#include "verilated.h"

// INCLUDE MODEL CLASS

#include "Vcounter_8bit.h"

// INCLUDE MODULE CLASSES
#include "Vcounter_8bit___024root.h"

// SYMS CLASS (contains all model state)
class alignas(VL_CACHE_LINE_BYTES)Vcounter_8bit__Syms final : public VerilatedSyms {
  public:
    // INTERNAL STATE
    Vcounter_8bit* const __Vm_modelp;
    bool __Vm_activity = false;  ///< Used by trace routines to determine change occurred
    uint32_t __Vm_baseCode = 0;  ///< Used by trace routines when tracing multiple models
    VlDeleter __Vm_deleter;
    bool __Vm_didInit = false;

    // MODULE INSTANCE STATE
    Vcounter_8bit___024root        TOP;

    // CONSTRUCTORS
    Vcounter_8bit__Syms(VerilatedContext* contextp, const char* namep, Vcounter_8bit* modelp);
    ~Vcounter_8bit__Syms();

    // METHODS
    const char* name() { return TOP.name(); }
};

#endif  // guard
