const fileupload=document.getElementById('file-upload');
const filename=document.getElementById('file-name');
fileupload.addEventListener('change',function()
{
    if(fileupload.files.length>0)
    {
        filename.textContent=fileupload.files[0].name;
       
    }
    else{
        filename.textContent='';
    }
    
});