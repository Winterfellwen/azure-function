$TenantId ="937d19e2-3481-443b-b230-38803a968598"
$ApplicationId = "a612ea48-5e33-4911-a44b-2a4ee3225fb7"
$PWord = "NkH8Q~uIKp7mr6jvmGWVvbA4pU42K1wuZ5VO5bmU"
$SecuredPassword = ConvertTo-SecureString -String $PWord -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $ApplicationId, $SecuredPassword
Connect-AzAccount -ServicePrincipal -TenantId $TenantId -Credential $Credential | out-null

$result = get-azvm
get-azvm

write-host "test" 
write-host $result
