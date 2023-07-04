cd /home/azuser/.Azure
$keyfile = get-content keystore.cache | ConvertFrom-Json
$keyfile.keyStoreValue.trim('"')
$keybase =$keyfile.keyStoreKey | ConvertFrom-json

$TenantId = $keybase.tenantId
$ApplicationId = $keybase.appId
$PWord = $keyfile.keyStoreValue.trim('"')
$SecuredPassword = ConvertTo-SecureString -String $PWord -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $ApplicationId, $SecuredPassword
Connect-AzAccount -ServicePrincipal -TenantId $TenantId -Credential $Credential -WarningAction ignore| out-null

$result = get-azvm | Out-String

write-host "test: get-azvm" 
write-host $result

Disconnect-AzAccount| out-null
