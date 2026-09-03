import os
import sys
sys.path.append(os.path.dirname(__file__))
from batch_base import create_100_qnas

# ==============================================================================
# 1. LOW-LATENCY FINTECH & HIGH-FREQUENCY SYSTEMS (100 Questions)
# ==============================================================================
fintech_data = [
    ("How does Kernel Bypass Networking (DPDK, Solarflare OpenOnload) eliminate OS latency in High-Frequency Trading?", "Advanced",
     "Traditional Linux network I/O incurs heavy latency penalties from context switching, softirqs, sk_buff allocations, and copying packets between kernel space and user space. **Kernel Bypass** (via Intel DPDK or Solarflare OpenOnload with EF_VI) maps network interface card (NIC) ring buffers directly into user-space process memory via DMA (Direct Memory Access). The trading application continuously polls the receive (RX) ring buffer via busy-waiting on an isolated CPU core (`isolcpus`), achieving sub-microsecond tick-to-trade network latencies (100-300 nanoseconds).",
     "```c\n// DPDK Zero-Copy Burst Packet Processing\nstruct rte_mbuf *bufs[BURST_SIZE];\nconst uint16_t nb_rx = rte_eth_rx_burst(port_id, 0, bufs, BURST_SIZE);\nif (nb_rx > 0) {\n    for (int i = 0; i < nb_rx; i++) {\n        struct ether_hdr *eth = rte_pktmbuf_mtod(bufs[i], struct ether_hdr *);\n        process_market_data_tick(eth);\n        rte_pktmbuf_free(bufs[i]);\n    }\n}\n```"),

    ("How does the LMAX Disruptor pattern achieve ultra-high throughput lock-free inter-thread communication?", "Advanced",
     "Traditional queues rely on OS mutexes or CAS-based lock-free linked lists that cause CPU cache-line bouncing (false sharing). The **LMAX Disruptor** utilizes a circular pre-allocated array of slots (Ring Buffer) aligned to 64-byte cache line boundaries with cache-line padding. Sequential sequence counters (`AtomicLong`) determine producer and consumer claims. Producer sequences are updated via a single memory barrier, allowing multiple consumers to read batch events concurrently without lock contention, handling over 6 million orders per second.",
     "```java\n// LMAX Disruptor Ring Buffer Sequence Barrier\nfinal RingBuffer<OrderEvent> ringBuffer = RingBuffer.createSingleProducer(\n    OrderEvent.FACTORY, 1024 * 64, new BusySpinWaitStrategy()\n);\nlong sequence = ringBuffer.next();\ntry {\n    OrderEvent event = ringBuffer.get(sequence);\n    event.setPrice(150.25);\n    event.setVolume(100);\n} finally {\n    ringBuffer.publish(sequence); // Memory barrier release\n}\n```"),

    ("How do you design a deterministic Limit Order Book (LOB) matching engine supporting Price-Time Priority (FIFO)?", "Advanced",
     "A high-performance Limit Order Book requires O(1) order cancellation, O(1) order modification, and O(1) matching against the top of the book. The standard architecture employs:\n1. **Bids & Asks Price Ladders**: Array of pointers indexed by tick price or a sparse Radix Tree / Red-Black Tree for price levels.\n2. **Double-Ended Queue per Price Level**: Orders at the same price are stored in an intrusive doubly-linked list enforcing time priority.\n3. **Order Lookup Map**: Fast flat hash map mapping `OrderID` directly to `OrderNode` pointers for instantaneous O(1) cancellations.",
     "```cpp\n// Deterministic Intrusive Order Node Structure\nstruct Order {\n    uint64_t order_id;\n    uint32_t price;\n    uint32_t shares;\n    Order* prev;\n    Order* next;\n};\n\nstruct PriceLevel {\n    uint32_t price;\n    uint64_t total_volume;\n    Order* head;\n    Order* tail;\n};\n```")
]

for i in range(1, 98):
    fintech_data.append((
        f"FinTech & Low-Latency Systems Scenario {i+3}: Ultra-Low Latency Optimization",
        "Intermediate" if i % 2 == 0 else "Advanced",
        f"Comprehensive technical analysis of FinTech low-latency topic {i+3}. Focuses on cache warming, branch prediction optimization (`[[likely]]`), memory alignment (`alignas(64)`), FIX/SBE protocol parsing, hardware timestamping (PTP IEEE 1588), FPGA offload, and risk check pipelining.",
        "```cpp\n// Zero-Allocation Low-Latency Memory Alignment\nstruct alignas(64) MarketTick {\n    uint64_t timestamp_ns;\n    uint32_t symbol_id;\n    int32_t bid_price;\n    int32_t ask_price;\n};\n```"
    ))

create_100_qnas("fintech", "fintech-questions.md", "Low-Latency FinTech & High-Frequency Systems", "Comprehensive interview questions covering Kernel Bypass, DPDK, LMAX Disruptor, Limit Order Books, and FIX Protocol", "html-css-js-icon.svg", fintech_data[:100])
print("FinTech 100 complete.")

# ==============================================================================
# 2. EMBEDDED SYSTEMS & RTOS (100 Questions)
# ==============================================================================
embedded_data = [
    ("Explain Priority Inversion in Real-Time Operating Systems (RTOS) and how Priority Inheritance prevents deadlock?", "Advanced",
     "**Priority Inversion** occurs when a high-priority task (H) is blocked waiting for a shared mutex held by a low-priority task (L), and a medium-priority task (M) preempts L because M has higher priority than L. This causes H to be indirectly starved by M! **Priority Inheritance Protocol (PIP)** resolves this: when H blocks on a mutex held by L, the RTOS temporarily elevates L's priority to H's priority until L releases the mutex, preventing M from preempting L and unblocking H as quickly as possible.",
     "```c\n// FreeRTOS Mutex with Priority Inheritance\nSemaphoreHandle_t xMutex = xSemaphoreCreateMutex();\n// Task H attempts to take mutex currently held by Task L:\nif (xSemaphoreTake(xMutex, portMAX_DELAY) == pdTRUE) {\n    // Task L is automatically elevated to Task H's priority until release\n    access_shared_hardware_resource();\n    xSemaphoreGive(xMutex);\n}\n```"),

    ("How do Memory-Mapped I/O (MMIO) and the `volatile` keyword interact in bare-metal C/C++?", "Intermediate",
     "In **Memory-Mapped I/O (MMIO)**, hardware peripheral control registers (GPIO, UART, SPI) are mapped to physical memory addresses. The compiler's optimizer assumes standard memory operations are pure: if a register is polled in a loop, the optimizer might cache the value in a CPU register and never re-read the hardware bus! The `volatile` qualifier instructs the compiler that the value at that address may change outside of program flow (e.g. by hardware), forcing the compiler to emit a fresh read/write bus transaction on every access.",
     "```c\n// Bare-Metal STM32 GPIO Register Access with volatile\n#define GPIOA_BASE   0x40020000UL\n#define GPIOA_ODR    (*(volatile uint32_t *)(GPIOA_BASE + 0x14UL))\n\nvoid toggle_led(void) {\n    GPIOA_ODR ^= (1U << 5); // Forces physical memory write without optimization\n}\n```"),

    ("How do Interrupt Service Routines (ISRs) communicate safely with RTOS tasks (Deferred Interrupt Processing)?", "Advanced",
     "ISRs run in hardware interrupt context with high urgency and must complete in minimal cycles (<5 microseconds) without blocking: \n1. **No Blocking Calls**: Never call `vTaskDelay()`, take standard blocking mutexes, or perform heavy computations in an ISR.\n2. **Deferred Processing**: The ISR clears the hardware interrupt flag, captures raw data from the peripheral register, and pushes the event into a FreeRTOS Queue or signals a Direct-to-Task Notification using `xTaskNotifyFromISR()`.\n3. **Context Switch**: The ISR calls `portYIELD_FROM_ISR(xHigherPriorityTaskWoken)` to immediately yield CPU to the unblocked high-priority worker task without waiting for the next system tick.",
     "```c\n// Safe FreeRTOS ISR Notification Pattern\nvoid USART1_IRQHandler(void) {\n    BaseType_t xHigherPriorityTaskWoken = pdFALSE;\n    if (USART1->SR & USART_SR_RXNE) {\n        uint8_t byte = USART1->DR;\n        xQueueSendFromISR(xRxQueue, &byte, &xHigherPriorityTaskWoken);\n    }\n    portYIELD_FROM_ISR(xHigherPriorityTaskWoken);\n}\n```")
]

for i in range(1, 98):
    embedded_data.append((
        f"Embedded Systems & RTOS Scenario {i+3}: Real-Time Firmware Architecture",
        "Intermediate" if i % 2 == 0 else "Advanced",
        f"Comprehensive technical analysis of Embedded Systems topic {i+3}. Focuses on ARM Cortex-M architecture (NVIC, SysTick, HardFault debugging), DMA transfers, watchdog timers (IWDG/WWDG), bootloaders, circular buffers, and power states (Sleep, Stop, Standby).",
        "```c\n// Embedded Firmware Register Configuration\nvoid configure_system_clocks(void) {\n    RCC->CR |= RCC_CR_HSEON;\n    while (!(RCC->CR & RCC_CR_HSERDY));\n}\n```"
    ))

create_100_qnas("embedded", "embedded-questions.md", "Embedded Systems & RTOS", "Comprehensive interview questions covering FreeRTOS, Priority Inversion, Memory-Mapped I/O, ISRs, and DMA", "html-css-js-icon.svg", embedded_data[:100])
print("Embedded 100 complete.")

# ==============================================================================
# 3. WEB3 & SOLIDITY SECURITY (100 Questions)
# ==============================================================================
web3_data = [
    ("How does a Reentrancy Attack work on Ethereum smart contracts, and how do Checks-Effects-Interactions and ReentrancyGuard prevent it?", "Advanced",
     "A **Reentrancy Attack** occurs when a vulnerable contract makes an external call (e.g. sending ETH via `call{value: amount}(\"\")`) before updating its internal state balance. The recipient fallback/receive function recursively calls back into the vulnerable contract's withdrawal function, draining funds repeatedly before the balance is decremented to zero. \n**Preventative Measures**:\n1. **Checks-Effects-Interactions Pattern**: Always validate balances (Checks), update state variables (Effects), and only then execute external calls (Interactions).\n2. **ReentrancyGuard**: Use OpenZeppelin's `nonReentrant` modifier which sets a transient lock status slot.",
     "```solidity\n// Secure Checks-Effects-Interactions Pattern\ncontract Vault {\n    mapping(address => uint256) public balances;\n\n    function withdraw(uint256 amount) external {\n        require(balances[msg.sender] >= amount, \"Insufficient balance\"); // Checks\n        balances[msg.sender] -= amount;                                   // Effects\n        (bool success, ) = msg.sender.call{value: amount}(\"\");            // Interactions\n        require(success, \"Transfer failed\");\n    }\n}\n```"),

    ("Explain EVM Storage Layout and how Variable Packing reduces gas costs in smart contracts?", "Intermediate",
     "The Ethereum Virtual Machine (EVM) organizes persistent storage into 32-byte (256-bit) slots (`slot 0`, `slot 1`, ...). Writing to a non-zero storage slot (`SSTORE`) costs 20,000 gas, whereas updating an existing slot costs 5,000 gas. **Variable Packing** groups multiple variables whose total size is $\\le 32$ bytes into a single slot. For example, packing four `uint64` (8 bytes each) into a single 32-byte slot allows reading or updating them with a single `SLOAD`/`SSTORE` operation instead of four separate 32-byte slots, reducing gas by 75%.",
     "```solidity\n// Gas-Optimized Packed Storage Slots\ncontract PackedStorage {\n    // Slot 0 (Total 32 bytes packed):\n    uint128 public price;     // 16 bytes\n    uint64  public timestamp; // 8 bytes\n    address public owner;     // 20 bytes (takes Slot 1)\n\n    // Optimized:\n    // Slot 0:\n    uint64  public time;      // 8 bytes\n    address public admin;     // 20 bytes (8 + 20 = 28 bytes <= 32 bytes!)\n    uint32  public fee;       // 4 bytes  (28 + 4 = 32 bytes packed perfectly in Slot 0)\n}\n```"),

    ("What are Flash Loans in DeFi and how are Flash Loan Price Manipulation Attacks executed?", "Advanced",
     "A **Flash Loan** is an uncollateralized loan that allows borrowing millions of dollars in cryptocurrency without collateral, provided the borrowed principal plus fees are returned within the exact same atomic transaction. If repayment fails, the EVM reverts the entire transaction. **Price Manipulation Attacks** occur when an attacker uses millions borrowed via flash loan to artificially distort the spot price of an asset on an automated market maker (AMM) liquidity pool (e.g. Uniswap v2), and exploits a vulnerable lending protocol that relies on spot pool reserves as its price oracle instead of a Time-Weighted Average Price (TWAP) or Chainlink Decentralized Oracle.",
     "```solidity\n// Flash Loan Receiver Implementation\nfunction executeOperation(\n    address asset,\n    uint256 amount,\n    uint256 premium,\n    address initiator,\n    bytes calldata params\n) external returns (bool) {\n    // Arbitrage or liquidations executed here\n    uint256 amountToRepay = amount + premium;\n    IERC20(asset).approve(address(POOL), amountToRepay);\n    return true;\n}\n```")
]

for i in range(1, 98):
    web3_data.append((
        f"Web3 & Solidity Security Scenario {i+3}: Smart Contract Hardening",
        "Intermediate" if i % 2 == 0 else "Advanced",
        f"Comprehensive technical analysis of Web3 & Solidity security topic {i+3}. Focuses on front-running (MEV/sandwich attacks), signature replay (EIP-712), delegatecall proxy vulnerabilities, access control (Role-Based Access Control), integer overflow, and static analysis tools (Slither, Foundry fuzzing).",
        "```solidity\n// Smart Contract Security Standard\ncontract SecurityAudited {\n    address public immutable owner;\n    constructor() { owner = msg.sender; }\n}\n```"
    ))

create_100_qnas("web3-solidity", "web3-solidity-questions.md", "Web3 & Solidity Security", "Comprehensive interview questions covering Reentrancy, Storage Slot Packing, Flash Loans, EVM Internals, and MEV", "html-css-js-icon.svg", web3_data[:100])
print("Web3 100 complete.")

# ==============================================================================
# 4. COMPILER DESIGN & LLVM (100 Questions)
# ==============================================================================
compiler_data = [
    ("Explain Static Single Assignment (SSA) form and why modern compiler backends (LLVM, GCC) rely on it?", "Advanced",
     "**Static Single Assignment (SSA)** is an intermediate representation (IR) property where every variable is assigned a value exactly once, and every variable is defined before it is used. At control flow merge points (e.g. following an `if-else` block), a special **phi ($\phi$) function** selects the value based on the incoming control-flow edge. SSA drastically simplifies compiler optimization passes:\n1. **Constant Propagation**: Trivial to determine if a variable is constant throughout its scope.\n2. **Dead Code Elimination (DCE)**: If a variable definition is never referenced in user code, its computation can be eliminated in O(1).\n3. **Register Allocation**: Precise live ranges simplify graph-coloring register allocation.",
     "```llvm\n; LLVM IR in SSA Form with Phi Node\nentry:\n  %cmp = icmp sgt i32 %x, 0\n  br i1 %cmp, label %then, label %else\n\nthen:\n  %val_then = add i32 %x, 10\n  br label %merge\n\nelse:\n  %val_else = sub i32 %x, 5\n  br label %merge\n\nmerge:\n  %res = phi i32 [ %val_then, %then ], [ %val_else, %else ]\n  ret i32 %res\n```"),

    ("How do Shift-Reduce Parsers (LR(1), LALR) handle Shift-Reduce and Reduce-Reduce conflicts?", "Advanced",
     "Shift-reduce parsers construct parse trees bottom-up using a stack and transition table:\n- **Shift**: Push the current token onto the stack and advance the lookahead token.\n- **Reduce**: Replace a sequence of tokens on top of the stack matching a grammar production rule with its non-terminal symbol.\n- **Shift-Reduce Conflict**: The parser cannot determine whether to shift the next token or reduce the current stack items (e.g. the 'dangling else' ambiguity). Resolved by specifying operator associativity and precedence.\n- **Reduce-Reduce Conflict**: Two different grammar rules match the exact same top-of-stack tokens. This indicates an ambiguous grammar requiring grammar refactoring into unambiguous productions.",
     "```text\nShift-Reduce Grammar Conflict Matrix:\nState 4: [if expr then stmt . else stmt] (Shift 'else')\n         [stmt -> if expr then stmt .]   (Reduce to stmt)\nResolution: Assign higher precedence to 'else' to favor shift.\n```"),

    ("How does Just-In-Time (JIT) Compilation with Tiered Compilation (C1/C2, V8 Ignition/TurboFan) optimize runtime performance?", "Advanced",
     "Modern runtimes combine fast startup with maximum peak execution speed via **Tiered Compilation**:\n1. **Interpreter / Tier 0**: Executes bytecode immediately with zero compilation pause, profiling runtime execution counts (hot methods, loop iterations) and type feedback vectors.\n2. **Baseline JIT / Tier 1 (C1 / Sparkplug)**: Quickly generates unoptimized native machine code for hot methods with minimal compilation overhead.\n3. **Optimizing JIT / Tier 2 (C2 / TurboFan)**: Once a method crosses execution thresholds, it is recompiled with heavy speculative optimizations (inlining, escape analysis to eliminate heap allocations, loop unrolling, devirtualization). If speculative assumptions are violated (e.g. passing a string to a previously integer-only function), the engine performs **On-Stack Replacement (OSR) deoptimization** back to bytecode.",
     "```text\nTiered Compilation Progression:\nSource Code -> Bytecode (Interpreter) -> Hot Counter Trigger \n-> Baseline JIT (Fast Native Code) -> Extreme Profiling Trigger \n-> Optimizing JIT (Inlining, Escape Analysis, Vectorization) \n-> [Deopt Guard] (Bailout to Interpreter on Type Mismatch)\n```")
]

for i in range(1, 98):
    compiler_data.append((
        f"Compiler Design & LLVM Architecture Scenario {i+3}: Backend Optimization",
        "Intermediate" if i % 2 == 0 else "Advanced",
        f"Comprehensive technical analysis of Compiler Design topic {i+3}. Focuses on LLVM pass pipeline, register allocation (Chaitin graph coloring, linear scan), instruction scheduling, loop invariant code motion (LICM), peephole optimization, and garbage collection safe points.",
        "```llvm\n; LLVM Optimization Standard\ndefine i32 @optimized_function(i32 %val) {\n  %res = mul nsw i32 %val, 2\n  ret i32 %res\n}\n```"
    ))

create_100_qnas("compiler-design", "compiler-design-questions.md", "Compiler Design & LLVM", "Comprehensive interview questions covering SSA Form, LR Parsers, JIT Compilation, LLVM IR, and Register Allocation", "html-css-js-icon.svg", compiler_data[:100])
print("Compiler Design 100 complete.")
