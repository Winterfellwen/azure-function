$result = get-azvm | Out-String

write-host "test: get-azvm" 
write-host $result

Disconnect-AzAccount| out-null
