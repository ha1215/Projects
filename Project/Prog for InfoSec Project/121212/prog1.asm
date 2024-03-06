.data
a dd 6
b dd 2

.code
main proc
    mov eax, dword ptr [b] 
    add eax, 2
    mov dword ptr [a], eax
    lea eax, [a]
    main endp
end
