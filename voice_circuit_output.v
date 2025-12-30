module logic_circuit (
    input A,
    input B,
    input C,
    output Y
);
    assign Y = (A & B) | (~C);
endmodule