import os
import time

def getNewFileName():
    file_no = 0
    for foldername, subfolders, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            if (filename[:8] == "schedule"):
                file_no = int(filename[8]) + 1
    return file_no
	
file_num = getNewFileName()
file_name = "schedule" + str(file_num) + ".html"
print(file_name)
handle = open(file_name, "a+")
handle.write('''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!-- saved from url=(0050)file:///C:/Users/liarh/Desktop/Plans/2-22-1/1.html -->
<html xmlns="http://www.w3.org/1999/xhtml"><head id="Head1"><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><title>
	Academic Planner
</title><link href="file:///C:/Users/liarh/Desktop/Plans/2-22-1/PacificBlue.css" type="text/css" rel="stylesheet">
		<script type="text/javascript" src="file:///C:/Users/liarh/Desktop/Plans/2-22-1/Messages.js.download"></script>
		<script type="text/javascript" src="file:///C:/Users/liarh/Desktop/Plans/2-22-1/common.js.download"></script>
		<script type="text/javascript">
			var dirtyFlag = false;	// true if changes have been made to a plan.
			var selIndex = 0;
				
			// Coordinates the state of the Save button with the new plan name text box.
			function DoChangeNewPlanName(box) {
				var ctl = document.getElementById("B_Save");
				if (ctl != null) {
					ctl.disabled = Trim(box.value).length < 1;
				}
				SetDirty();
			}
			
			// Sets the flag that tracks whether changes have been made to the current plan.
			function SetDirty(dirty) {
				if (dirty == null) {
					dirtyFlag = true;
				} else {
					dirtyFlag = dirty;
				}
			}
			
			// Returns the current value of the dirty flag.
			function IsDirty() {
				return dirtyFlag;
			}
			
			// Prompts the user if changes have been made to a plan, and the user
			// has taken an action that would cause the changes to be discarded.
			function ConfirmDiscard() {
				if (IsDirty()) {
					return confirm("Ok to discard changes?");
				}else{
					return true;
				}
			}
			
			// Causes prompt to user to discard changes when the user has made
			// changes to the current plan, has not saved them, and is selecting a 
			// different plan from the dropdown listbox.
			function ChangePlans(selbox) {
				var rtn = true;
				if (selbox.selectedIndex != selIndex) {
					if (!ConfirmDiscard()) {
						selbox.selectedIndex = selIndex;
						rtn = false;
					}
				}
				return rtn;			
			}
			
			function ConfirmDelete(){
				if(confirm(GetMessage("7508"))){		// Are you sure you want to delete this plan? Click cancel to abort delete.
					return true;
				}
				return false;
			}
			
			function setSid(){
				try{
					var stuId = window.parent.frames['btnbar'].document.forms[0].hidSID.value;
					if (stuId != null && stuId.length == 9)
						document.forms[0].studentID.value = stuId;
				}
				catch(ex){}
			}
			function checkSid(){
				with (document.forms[0]){
					return (studentID != null && studentID.value.length == 9)?true:false;
				}
			}
			
			// Page initialization routine.  Saves the current selection from the 
			// plan dropdown listbox.  Sets the initial focus to the correct field.
			function InitPage() {
				var list = document.getElementById("DD_PlanTitle");
				var ctl = document.getElementById("TB_NewPlanName");

				if (list != null) {
					selIndex = list.selectedIndex;
				}
				if (ctl != null && !ctl.disabled && !ctl.hidden) {
					ctl.focus();
				}
				HighlightAutoTab(false);
			}	
			
		</script>
</head>
<body bgcolor="lightsteelblue" onload="InitPage()" tabindex="-1">
    <form name="acadplan" method="post" action="https://www.wctcs.ctc.edu/DAAdminWeb/Planner.aspx?studentID=" id="acadplan">
<div>
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="">
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="">
<input type="hidden" name="__LASTFOCUS" id="__LASTFOCUS" value="">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKLTcxMjc4NjQ5OQ9kFgICAw9kFjoCAQ9kFgJmDxYCHgdvbmNsaWNrBY4Bd2luZG93Lm9wZW4oJ2hlbHAvYWR2aXNvci9oZWxwX0FjYWRQbGFuci5odG0nLCd3aW4xJywnd2lkdGg9NDg2LGhlaWdodD0zNzUsc2NyZWVuWD0xMDAsc2NyZWVuWT0xMDAsbGVmdD0xMDAsdG9wPTEwMCxzY3JvbGxiYXJzJyk7cmV0dXJuIGZhbHNlOxYCAgEPFgYeBmhlaWdodAUCMjceBXdpZHRoBQIyNx4Dc3JjBRd+L2ltYWdlcy9oZWxwX2ljb241LmdpZmQCAg8PFgIeBFRleHQFHFBsYW46IEVFIE9SIENJViBFTkcgSkcgVzIwMTdkZAIDDw8WBB8EBSYmbmJzcDtQbGFuJm5ic3A7TmFtZSZuYnNwOw0KCQkJCQkJCQkJCR4HVmlzaWJsZWhkZAIEDw8WAh8FaBYCHgdvbmtleXVwBRpEb0NoYW5nZU5ld1BsYW5OYW1lKHRoaXMpO2QCBg8PZBYCHwAFGHJldHVybiBDb25maXJtRGlzY2FyZCgpO2QCBw8PZBYCHwAFGHJldHVybiBDb25maXJtRGlzY2FyZCgpO2QCCA8PZBYCHwAFF3JldHVybiBDb25maXJtRGVsZXRlKCk7ZAIJDw9kFgIfAAUPd2luZG93LnByaW50KCk7ZAILDxAPZBYCHghvbmNoYW5nZQUmaWYgKCFDaGFuZ2VQbGFucyh0aGlzKSl7cmV0dXJuIGZhbHNlO30QFQEWRUUgT1IgQ0lWIEVORyBKRyBXMjAxNxUBBTE5ODgzFCsDAWcWAWZkAg4PZBYMAgEPDxYCHwQFC1NwcmluZyAyMDE3ZGQCAw8PFgIeCFRhYkluZGV4AR0AFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0eB29uZm9jdXMFVGlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMV9UQl9MaW5lMScsICdRUDFfVEJfTGluZTInLCA0MCl9O2QCBQ8PFgIfCAEeABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVGlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMV9UQl9MaW5lMicsICdRUDFfVEJfTGluZTMnLCA0MCl9O2QCBw8PFgIfCAEfABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVGlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMV9UQl9MaW5lMycsICdRUDFfVEJfTGluZTQnLCA0MCl9O2QCCQ8PFgIfCAEgABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVGlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMV9UQl9MaW5lNCcsICdRUDFfVEJfTGluZTUnLCA0MCl9O2QCCw8PFgIfCAEhABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVGlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMV9UQl9MaW5lNScsICdRUDJfVEJfTGluZTEnLCA0MCl9O2QCDw9kFgwCAQ8PFgIfBAULU3VtbWVyIDIwMTdkZAIDDw8WAh8IASIAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVUaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVAyX1RCX0xpbmUxJywgJ1FQMl9UQl9MaW5lMicsIDQwKX07ZAIFDw8WAh8IASMAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVUaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVAyX1RCX0xpbmUyJywgJ1FQMl9UQl9MaW5lMycsIDQwKX07ZAIHDw8WAh8IASQAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVUaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVAyX1RCX0xpbmUzJywgJ1FQMl9UQl9MaW5lNCcsIDQwKX07ZAIJDw8WAh8IASUAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVUaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVAyX1RCX0xpbmU0JywgJ1FQMl9UQl9MaW5lNScsIDQwKX07ZAILDw8WAh8IASYAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVUaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVAyX1RCX0xpbmU1JywgJ1FQM19UQl9MaW5lMScsIDQwKX07ZAIQD2QWDAIBDw8WAh8EBQtGYWxsIDIwMTcgIGRkAgMPDxYCHwgBJwAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVRpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDNfVEJfTGluZTEnLCAnUVAzX1RCX0xpbmUyJywgNDApfTtkAgUPDxYCHwgBKAAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVRpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDNfVEJfTGluZTInLCAnUVAzX1RCX0xpbmUzJywgNDApfTtkAgcPDxYCHwgBKQAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVRpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDNfVEJfTGluZTMnLCAnUVAzX1RCX0xpbmU0JywgNDApfTtkAgkPDxYCHwgBKgAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVRpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDNfVEJfTGluZTQnLCAnUVAzX1RCX0xpbmU1JywgNDApfTtkAgsPDxYCHwgBKwAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVRpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDNfVEJfTGluZTUnLCAnUVA0X1RCX0xpbmUxJywgNDApfTtkAhEPZBYMAgEPDxYCHwQFC1dpbnRlciAyMDE4ZGQCAw8PFgIfCAEsABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVGlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQNF9UQl9MaW5lMScsICdRUDRfVEJfTGluZTInLCA0MCl9O2QCBQ8PFgIfCAEtABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVGlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQNF9UQl9MaW5lMicsICdRUDRfVEJfTGluZTMnLCA0MCl9O2QCBw8PFgIfCAEuABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVGlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQNF9UQl9MaW5lMycsICdRUDRfVEJfTGluZTQnLCA0MCl9O2QCCQ8PFgIfCAEvABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVGlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQNF9UQl9MaW5lNCcsICdRUDRfVEJfTGluZTUnLCA0MCl9O2QCCw8PFgIfCAEwABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVGlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQNF9UQl9MaW5lNScsICdRUDVfVEJfTGluZTEnLCA0MCl9O2QCEg9kFgwCAQ8PFgIfBAULU3ByaW5nIDIwMThkZAIDDw8WAh8IATEAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVUaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVA1X1RCX0xpbmUxJywgJ1FQNV9UQl9MaW5lMicsIDQwKX07ZAIFDw8WAh8IATIAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVUaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVA1X1RCX0xpbmUyJywgJ1FQNV9UQl9MaW5lMycsIDQwKX07ZAIHDw8WAh8IATMAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVUaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVA1X1RCX0xpbmUzJywgJ1FQNV9UQl9MaW5lNCcsIDQwKX07ZAIJDw8WAh8IATQAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVUaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVA1X1RCX0xpbmU0JywgJ1FQNV9UQl9MaW5lNScsIDQwKX07ZAILDw8WAh8IATUAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVUaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVA1X1RCX0xpbmU1JywgJ1FQNl9UQl9MaW5lMScsIDQwKX07ZAITD2QWDAIBDw8WAh8EBQtTdW1tZXIgMjAxOGRkAgMPDxYCHwgBNgAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVRpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDZfVEJfTGluZTEnLCAnUVA2X1RCX0xpbmUyJywgNDApfTtkAgUPDxYCHwgBNwAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVRpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDZfVEJfTGluZTInLCAnUVA2X1RCX0xpbmUzJywgNDApfTtkAgcPDxYCHwgBOAAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVRpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDZfVEJfTGluZTMnLCAnUVA2X1RCX0xpbmU0JywgNDApfTtkAgkPDxYCHwgBOQAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVRpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDZfVEJfTGluZTQnLCAnUVA2X1RCX0xpbmU1JywgNDApfTtkAgsPDxYCHwgBOgAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVRpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDZfVEJfTGluZTUnLCAnUVA3X1RCX0xpbmUxJywgNDApfTtkAhQPZBYMAgEPDxYCHwQFC0ZhbGwgMjAxOCAgZGQCAw8PFgIfCAE7ABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVGlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQN19UQl9MaW5lMScsICdRUDdfVEJfTGluZTInLCA0MCl9O2QCBQ8PFgIfCAE8ABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVGlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQN19UQl9MaW5lMicsICdRUDdfVEJfTGluZTMnLCA0MCl9O2QCBw8PFgIfCAE9ABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVGlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQN19UQl9MaW5lMycsICdRUDdfVEJfTGluZTQnLCA0MCl9O2QCCQ8PFgIfCAE+ABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVGlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQN19UQl9MaW5lNCcsICdRUDdfVEJfTGluZTUnLCA0MCl9O2QCCw8PFgIfCAE/ABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVGlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQN19UQl9MaW5lNScsICdRUDhfVEJfTGluZTEnLCA0MCl9O2QCFQ9kFgwCAQ8PFgIfBAULV2ludGVyIDIwMTlkZAIDDw8WAh8IAUAAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVUaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVA4X1RCX0xpbmUxJywgJ1FQOF9UQl9MaW5lMicsIDQwKX07ZAIFDw8WAh8IAUEAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVUaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVA4X1RCX0xpbmUyJywgJ1FQOF9UQl9MaW5lMycsIDQwKX07ZAIHDw8WAh8IAUIAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVUaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVA4X1RCX0xpbmUzJywgJ1FQOF9UQl9MaW5lNCcsIDQwKX07ZAIJDw8WAh8IAUMAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVUaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVA4X1RCX0xpbmU0JywgJ1FQOF9UQl9MaW5lNScsIDQwKX07ZAILDw8WAh8IAUQAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVUaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVA4X1RCX0xpbmU1JywgJ1FQOV9UQl9MaW5lMScsIDQwKX07ZAIWD2QWDAIBDw8WAh8EBQtTcHJpbmcgMjAxOWRkAgMPDxYCHwgBRQAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVRpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDlfVEJfTGluZTEnLCAnUVA5X1RCX0xpbmUyJywgNDApfTtkAgUPDxYCHwgBRgAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVRpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDlfVEJfTGluZTInLCAnUVA5X1RCX0xpbmUzJywgNDApfTtkAgcPDxYCHwgBRwAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVRpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDlfVEJfTGluZTMnLCAnUVA5X1RCX0xpbmU0JywgNDApfTtkAgkPDxYCHwgBSAAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVRpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDlfVEJfTGluZTQnLCAnUVA5X1RCX0xpbmU1JywgNDApfTtkAgsPDxYCHwgBSQAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVVpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDlfVEJfTGluZTUnLCAnUVAxMF9UQl9MaW5lMScsIDQwKX07ZAIXD2QWDAIBDw8WAh8EBQtTdW1tZXIgMjAxOWRkAgMPDxYCHwgBSgAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDEwX1RCX0xpbmUxJywgJ1FQMTBfVEJfTGluZTInLCA0MCl9O2QCBQ8PFgIfCAFLABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTBfVEJfTGluZTInLCAnUVAxMF9UQl9MaW5lMycsIDQwKX07ZAIHDw8WAh8IAUwAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVWaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVAxMF9UQl9MaW5lMycsICdRUDEwX1RCX0xpbmU0JywgNDApfTtkAgkPDxYCHwgBTQAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDEwX1RCX0xpbmU0JywgJ1FQMTBfVEJfTGluZTUnLCA0MCl9O2QCCw8PFgIfCAFOABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTBfVEJfTGluZTUnLCAnUVAxMV9UQl9MaW5lMScsIDQwKX07ZAIYD2QWDAIBDw8WAh8EBQtGYWxsIDIwMTkgIGRkAgMPDxYCHwgBTwAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDExX1RCX0xpbmUxJywgJ1FQMTFfVEJfTGluZTInLCA0MCl9O2QCBQ8PFgIfCAFQABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTFfVEJfTGluZTInLCAnUVAxMV9UQl9MaW5lMycsIDQwKX07ZAIHDw8WAh8IAVEAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVWaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVAxMV9UQl9MaW5lMycsICdRUDExX1RCX0xpbmU0JywgNDApfTtkAgkPDxYCHwgBUgAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDExX1RCX0xpbmU0JywgJ1FQMTFfVEJfTGluZTUnLCA0MCl9O2QCCw8PFgIfCAFTABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTFfVEJfTGluZTUnLCAnUVAxMl9UQl9MaW5lMScsIDQwKX07ZAIZD2QWDAIBDw8WAh8EBQtXaW50ZXIgMjAyMGRkAgMPDxYCHwgBVAAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDEyX1RCX0xpbmUxJywgJ1FQMTJfVEJfTGluZTInLCA0MCl9O2QCBQ8PFgIfCAFVABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTJfVEJfTGluZTInLCAnUVAxMl9UQl9MaW5lMycsIDQwKX07ZAIHDw8WAh8IAVYAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVWaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVAxMl9UQl9MaW5lMycsICdRUDEyX1RCX0xpbmU0JywgNDApfTtkAgkPDxYCHwgBVwAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDEyX1RCX0xpbmU0JywgJ1FQMTJfVEJfTGluZTUnLCA0MCl9O2QCCw8PFgIfCAFYABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTJfVEJfTGluZTUnLCAnUVAxM19UQl9MaW5lMScsIDQwKX07ZAIaD2QWDAIBDw8WAh8EBQtTcHJpbmcgMjAyMGRkAgMPDxYCHwgBWQAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDEzX1RCX0xpbmUxJywgJ1FQMTNfVEJfTGluZTInLCA0MCl9O2QCBQ8PFgIfCAFaABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTNfVEJfTGluZTInLCAnUVAxM19UQl9MaW5lMycsIDQwKX07ZAIHDw8WAh8IAVsAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVWaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVAxM19UQl9MaW5lMycsICdRUDEzX1RCX0xpbmU0JywgNDApfTtkAgkPDxYCHwgBXAAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDEzX1RCX0xpbmU0JywgJ1FQMTNfVEJfTGluZTUnLCA0MCl9O2QCCw8PFgIfCAFdABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTNfVEJfTGluZTUnLCAnUVAxNF9UQl9MaW5lMScsIDQwKX07ZAIbD2QWDAIBDw8WAh8EBQtTdW1tZXIgMjAyMGRkAgMPDxYCHwgBXgAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDE0X1RCX0xpbmUxJywgJ1FQMTRfVEJfTGluZTInLCA0MCl9O2QCBQ8PFgIfCAFfABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTRfVEJfTGluZTInLCAnUVAxNF9UQl9MaW5lMycsIDQwKX07ZAIHDw8WAh8IAWAAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVWaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVAxNF9UQl9MaW5lMycsICdRUDE0X1RCX0xpbmU0JywgNDApfTtkAgkPDxYCHwgBYQAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDE0X1RCX0xpbmU0JywgJ1FQMTRfVEJfTGluZTUnLCA0MCl9O2QCCw8PFgIfCAFiABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTRfVEJfTGluZTUnLCAnUVAxNV9UQl9MaW5lMScsIDQwKX07ZAIcD2QWDAIBDw8WAh8EBQtGYWxsIDIwMjAgIGRkAgMPDxYCHwgBYwAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDE1X1RCX0xpbmUxJywgJ1FQMTVfVEJfTGluZTInLCA0MCl9O2QCBQ8PFgIfCAFkABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTVfVEJfTGluZTInLCAnUVAxNV9UQl9MaW5lMycsIDQwKX07ZAIHDw8WAh8IAWUAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVWaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVAxNV9UQl9MaW5lMycsICdRUDE1X1RCX0xpbmU0JywgNDApfTtkAgkPDxYCHwgBZgAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDE1X1RCX0xpbmU0JywgJ1FQMTVfVEJfTGluZTUnLCA0MCl9O2QCCw8PFgIfCAFnABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTVfVEJfTGluZTUnLCAnUVAxNl9UQl9MaW5lMScsIDQwKX07ZAIdD2QWDAIBDw8WAh8EBQtXaW50ZXIgMjAyMWRkAgMPDxYCHwgBaAAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDE2X1RCX0xpbmUxJywgJ1FQMTZfVEJfTGluZTInLCA0MCl9O2QCBQ8PFgIfCAFpABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTZfVEJfTGluZTInLCAnUVAxNl9UQl9MaW5lMycsIDQwKX07ZAIHDw8WAh8IAWoAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVWaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVAxNl9UQl9MaW5lMycsICdRUDE2X1RCX0xpbmU0JywgNDApfTtkAgkPDxYCHwgBawAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDE2X1RCX0xpbmU0JywgJ1FQMTZfVEJfTGluZTUnLCA0MCl9O2QCCw8PFgIfCAFsABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTZfVEJfTGluZTUnLCAnUVAxN19UQl9MaW5lMScsIDQwKX07ZAIeD2QWDAIBDw8WAh8EBQtTcHJpbmcgMjAyMWRkAgMPDxYCHwgBbQAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDE3X1RCX0xpbmUxJywgJ1FQMTdfVEJfTGluZTInLCA0MCl9O2QCBQ8PFgIfCAFuABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTdfVEJfTGluZTInLCAnUVAxN19UQl9MaW5lMycsIDQwKX07ZAIHDw8WAh8IAW8AFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVWaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVAxN19UQl9MaW5lMycsICdRUDE3X1RCX0xpbmU0JywgNDApfTtkAgkPDxYCHwgBcAAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDE3X1RCX0xpbmU0JywgJ1FQMTdfVEJfTGluZTUnLCA0MCl9O2QCCw8PFgIfCAFxABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTdfVEJfTGluZTUnLCAnUVAxOF9UQl9MaW5lMScsIDQwKX07ZAIfD2QWDAIBDw8WAh8EBQtTdW1tZXIgMjAyMWRkAgMPDxYCHwgBcgAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDE4X1RCX0xpbmUxJywgJ1FQMThfVEJfTGluZTInLCA0MCl9O2QCBQ8PFgIfCAFzABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMThfVEJfTGluZTInLCAnUVAxOF9UQl9MaW5lMycsIDQwKX07ZAIHDw8WAh8IAXQAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVWaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVAxOF9UQl9MaW5lMycsICdRUDE4X1RCX0xpbmU0JywgNDApfTtkAgkPDxYCHwgBdQAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDE4X1RCX0xpbmU0JywgJ1FQMThfVEJfTGluZTUnLCA0MCl9O2QCCw8PFgIfCAF2ABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMThfVEJfTGluZTUnLCAnUVAxOV9UQl9MaW5lMScsIDQwKX07ZAIgD2QWDAIBDw8WAh8EBQtGYWxsIDIwMjEgIGRkAgMPDxYCHwgBdwAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDE5X1RCX0xpbmUxJywgJ1FQMTlfVEJfTGluZTInLCA0MCl9O2QCBQ8PFgIfCAF4ABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTlfVEJfTGluZTInLCAnUVAxOV9UQl9MaW5lMycsIDQwKX07ZAIHDw8WAh8IAXkAFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVWaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVAxOV9UQl9MaW5lMycsICdRUDE5X1RCX0xpbmU0JywgNDApfTtkAgkPDxYCHwgBegAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDE5X1RCX0xpbmU0JywgJ1FQMTlfVEJfTGluZTUnLCA0MCl9O2QCCw8PFgIfCAF7ABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMTlfVEJfTGluZTUnLCAnUVAyMF9UQl9MaW5lMScsIDQwKX07ZAIhD2QWDAIBDw8WAh8EBQtXaW50ZXIgMjAyMmRkAgMPDxYCHwgBfAAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDIwX1RCX0xpbmUxJywgJ1FQMjBfVEJfTGluZTInLCA0MCl9O2QCBQ8PFgIfCAF9ABYEHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9HwkFVmlmICh0eXBlb2YoYXV0b2p1bXApICE9ICd1bmRlZmluZWQnKSB7YXV0b2p1bXAoJ1FQMjBfVEJfTGluZTInLCAnUVAyMF9UQl9MaW5lMycsIDQwKX07ZAIHDw8WAh8IAX4AFgQfBwU4aWYgKHR5cGVvZihTZXREaXJ0eSkgIT0gJ3VuZGVmaW5lZCcpIHsgU2V0RGlydHkodHJ1ZSk7IH0fCQVWaWYgKHR5cGVvZihhdXRvanVtcCkgIT0gJ3VuZGVmaW5lZCcpIHthdXRvanVtcCgnUVAyMF9UQl9MaW5lMycsICdRUDIwX1RCX0xpbmU0JywgNDApfTtkAgkPDxYCHwgBfwAWBB8HBThpZiAodHlwZW9mKFNldERpcnR5KSAhPSAndW5kZWZpbmVkJykgeyBTZXREaXJ0eSh0cnVlKTsgfR8JBVZpZiAodHlwZW9mKGF1dG9qdW1wKSAhPSAndW5kZWZpbmVkJykge2F1dG9qdW1wKCdRUDIwX1RCX0xpbmU0JywgJ1FQMjBfVEJfTGluZTUnLCA0MCl9O2QCCw8PFgIfCAGAABYCHwcFOGlmICh0eXBlb2YoU2V0RGlydHkpICE9ICd1bmRlZmluZWQnKSB7IFNldERpcnR5KHRydWUpOyB9ZGSGp3y/4aCZQ8in48uZgnqqvoB5cg==">
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['acadplan'];
if (!theForm) {
    theForm = document.acadplan;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<div>

	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="DEE3BEA2">
	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEWbQL8i72nBQKvqOcaAtHu7osEAvnz+oUBAvDz+uIHAviyrZAOAo/kj6YHApTByXYCrou8ow8CsZ2UugICsZ2A3wkCsZ3sgwECsZ34gQ4CsZ3kpgUCyIyo+g8CyIyUnwcCyIyAxA4CyIyMwgsCyIz45gIC482P/gMC4837ogsC483nxwIC483zxQ8C483f6gYCkuWPhQwCkuX7qQMCkuXnzgoCkuXzzAcCkuXf8Q4Crab3CAKtpuOtBwKtps/SDgKtptvQCwKtpsf1AgK0kcYJArSRsq4HArSRntMOArSRqtELArSRlvYCAs/SrY0EAs/SmbILAs/ShdcCAs/SkdUPAs/S/fkGAu7lzWsC7uW5kAgC7uWltQ8C7uWxswwC7uWd2AMCiae17wQCiaehlAwCiaeNuQMCiaeZNwKJp4XcBwKT+brKCQKS+brKCQKR+brKCQKY+brKCQKX+brKCQKT+aa7BwKS+aa7BwKR+aa7BwKY+aa7BwKX+aa7BwKT+YLkBgKS+YLkBgKR+YLkBgKY+YLkBgKX+YLkBgKT+e78BAKS+e78BAKR+e78BAKY+e78BAKX+e78BAKT+aruBQKS+aruBQKR+aruBQKY+aruBQKX+aruBQKu4rT0DQKt4rT0DQKs4rT0DQKz4rT0DQKy4rT0DQKu4tCMCQKt4tCMCQKs4tCMCQKz4tCMCQKy4tCMCQKu4rylBwKt4rylBwKs4rylBwKz4rylBwKy4rylBwKT+ZrxDQKS+ZrxDQKR+ZrxDQKY+ZrxDQKX+ZrxDQKT+YbiCwKS+YbiCwKR+YbiCwKY+YbiCwKX+YbiCwKC6I/wAgKB6I/wAgKA6I/wAgKH6I/wAgKG6I/wAho4M+1E545ia0+7eg5ZVHfeFFVX">
</div>
	        <input type="hidden" id="studentID" name="studentID" value=" "> 
	        <input type="hidden" id="studentName" name="studentName">
			<input name="scroll" type="hidden" id="scroll" value="0"> 
			<input type="hidden" name="hidSelStu">
			<input type="hidden" name="hidDID">
			<table cellspacing="0" cellpadding="0" border="0">
				<tbody><tr>
					<td width="10">&nbsp;</td> <!-- provides a left margin for the page-->
					<td>
						<table cellspacing="0" cellpadding="0" border="0">
							<tbody><tr>
								
								
								<td nowrap="" width="50" class="hidPrint">
									<a href="https://www.wctcs.ctc.edu/DAAdminWeb/UserControls/#" id="ICO_Help_HREF_Help" accesskey="8" onclick="window.open(&#39;help/advisor/help_AcadPlanr.htm&#39;,&#39;win1&#39;,&#39;width=486,height=375,screenX=100,screenY=100,left=100,top=100,scrollbars&#39;);return false;">
	
</a>


								</td>
							</tr>
							<tr>
								<td nowrap="" width="50">&nbsp;</td>
							</tr>
						</tbody></table>
						<div class="hidScreen">
							<table cellspacing="0" cellpadding="0" border="0">
								<tbody><tr>
									<td nowrap="" width="50" rowspan="2">&nbsp;</td>
									<td valign="middle" nowrap="" align="center" width="555">
										<span id="LBL_PlanTitlePrint" class="screensubtitle_student">
''')
#										Plan: EE - JG
print("Give me a plan name. ")
plan_name = input()
print(plan_name)
time.sleep(1)
handle.write(plan_name)
print("Got past print for plan name")
time.sleep(1)
handle.write('''
										</span>
									    <span id="Parameters"> 
										  <span id="Major" style="display:block;">
''')
print("Give me a Major. ")
major = input()
handle.write(major)
handle.write('''
</span>
                                          <span id="School" style="display:block;">
''')
print("Give me a School. ")
school = input()
handle.write(school)
handle.write('''
</span>
                                          <span id="TimePreference" style="display:block;">
''')
print("Give me a time preference. ")
preference = input()
handle.write(preference)
handle.write('''
</span> 
                                          <span id="SummerPreference" style="display:block;">
''')
print("Summer classes? ")
summer_classes = input()
handle.write(summer_classes)
handle.write('''
</span> 
                                          <span id="StartQuarter" style="display:block;">
''')
print("Starting Quarter? ")
start_quarter = input()
handle.write(start_quarter)
handle.write('''
</span> 
										  <span id="StartMath" style="display:block;">
''')
# StartMath
print("Starting Math?")
start_math = input()
handle.write(start_math) 
handle.write('''
</span>
										  <span id="StartEngl" style="display:block;">
''')
#230
print("Starting English?")
start_english = input()
handle.write(start_english)
handle.write('''
</span>										  
                                          <span id="EnrollmentType" style="display:block;">
''')
#EnrollmentType
enrollment = input("Full or Part Time Enrollment?\n")
handle.write(enrollment)
handle.write('''
</span> 
                                          <span id="JobType" style="display:block;">
''')
#JobType
jobtype = input("Full or Part Time Job?\n")
handle.write(jobtype)
handle.write('''
</span> 
                                        </span> 
										<span id="Rank"> 
                                          <span id="Grade" style="display:block;">
''')
#Grade
grade = input("How good is this plan?\n")
handle.write(grade)
handle.write('''
</span> 
                                          <span id="Reason" style="display:block;">
''')
#Reason
reason = input("Reason for the grade?\n")
handle.write(reason)
handle.write('''
</span> 
                                        </span>
									</td>
									<td nowrap="" width="50">&nbsp;</td>
								</tr>
							</tbody></table>
							<table cellspacing="0" cellpadding="0" border="0">
								<tbody><tr>
									<td nowrap="" width="50" rowspan="2">&nbsp;</td>
									
									<td nowrap="" width="50">&nbsp;</td>
								</tr>
							</tbody></table>
						</div> 
						<div class="hidPrint" style="BORDER-RIGHT: 1px outset; PADDING-RIGHT: 5px; BORDER-TOP: 1px outset; PADDING-LEFT: 5px; PADDING-BOTTOM: 5px; MARGIN: 0px; BORDER-LEFT: 1px outset; WIDTH: 612px; PADDING-TOP: 5px; BORDER-BOTTOM: 1px outset; BACKGROUND-COLOR: lightgrey">
							<table cellspacing="0" cellpadding="0" width="617" border="0">
								<tbody><tr>
									<td valign="baseline" nowrap="" align="right" width="65"></td>
									<td nowrap="" align="left" width="200"></td>
									<td nowrap="" align="right">
										<input type="submit" name="B_Save" value="Save" id="B_Save" accesskey="S" tabindex="3">
										<input type="submit" name="B_New" value="New..." onclick="return ConfirmDiscard();" id="B_New" accesskey="N" tabindex="4">
										<input type="submit" name="B_Cancel" value="Clear" onclick="return ConfirmDiscard();" id="B_Cancel" accesskey="C" tabindex="5">
										<input type="submit" name="B_Delete" value="Delete" onclick="return ConfirmDelete();" id="B_Delete" accesskey="D" tabindex="6">
										<input type="submit" name="B_Print" value="Print..." onclick="window.print();" id="B_Print" accesskey="P" tabindex="7">
									</td>
								</tr>
							</tbody></table>
						</div>
						<div class="hidPrint" style="BORDER-RIGHT: 1px outset; BORDER-TOP: 1px outset; PADDING-RIGHT: 5px; BORDER-TOP: 1px outset; PADDING-LEFT: 5px; PADDING-BOTTOM: 5px; MARGIN: 0px; BORDER-LEFT: 1px outset; WIDTH: 612px; PADDING-TOP: 0px; BORDER-BOTTOM: 1px outset; BACKGROUND-COLOR: lightgrey">
							<table cellspacing="0" cellpadding="0" width="617" border="0">
								<tbody><tr>
									<td nowrap="">
										<table height="22" width="617" cellspacing="0" cellpadding="2" border="0">
											<tbody><tr>
												<td valign="middle" nowrap="" width="20" class="hidPrint"><span id="LBL_PlanTitle" style="display:inline-block;font-family:Arial;font-size:12px;width:20px;">Plan&nbsp;</span></td>
												<td width="240" nowrap="" class="hidPrint"><select name="DD_PlanTitle" onchange="if (!ChangePlans(this)){return false;};setTimeout(&#39;__doPostBack(\&#39;DD_PlanTitle\&#39;,\&#39;\&#39;)&#39;, 0)" id="DD_PlanTitle" tabindex="8" style="width:230px;">
	<option selected="selected" value="19883">EE OR CIV ENG JG W2017</option>

</select></td>
												<td valign="top" id="errIcon"></td>
												<td class="doctext" valign="top" width="352"></td>
											</tr>
										</tbody></table>
									</td>
								</tr>
								<tr>
									<td nowrap="">
										<table class="showPrint" cellspacing="2" cellpadding="0" width="617" border="0">
											<tbody><tr>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP1_LBL_QPlanTitle">Spring 2017</span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP1$TB_Line1" type="text" value="PHYS 233" maxlength="40" id="QP1_TB_Line1" tabindex="29" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP1_TB_Line1&#39;, &#39;QP1_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP1$TB_Line2" type="text" value=" " maxlength="40" id="QP1_TB_Line2" tabindex="30" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP1_TB_Line2&#39;, &#39;QP1_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP1$TB_Line3" type="text" value=" " maxlength="40" id="QP1_TB_Line3" tabindex="31" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP1_TB_Line3&#39;, &#39;QP1_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP1$TB_Line4" type="text" value=" " maxlength="40" id="QP1_TB_Line4" tabindex="32" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP1_TB_Line4&#39;, &#39;QP1_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP1$TB_Line5" type="text" value=" " maxlength="40" id="QP1_TB_Line5" tabindex="33" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP1_TB_Line5&#39;, &#39;QP2_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP2_LBL_QPlanTitle">Summer 2017</span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP2$TB_Line1" type="text" value=" " maxlength="40" id="QP2_TB_Line1" tabindex="34" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP2_TB_Line1&#39;, &#39;QP2_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP2$TB_Line2" type="text" value=" " maxlength="40" id="QP2_TB_Line2" tabindex="35" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP2_TB_Line2&#39;, &#39;QP2_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP2$TB_Line3" type="text" value=" " maxlength="40" id="QP2_TB_Line3" tabindex="36" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP2_TB_Line3&#39;, &#39;QP2_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP2$TB_Line4" type="text" value=" " maxlength="40" id="QP2_TB_Line4" tabindex="37" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP2_TB_Line4&#39;, &#39;QP2_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP2$TB_Line5" type="text" value=" " maxlength="40" id="QP2_TB_Line5" tabindex="38" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP2_TB_Line5&#39;, &#39;QP3_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
											</tr>
											<tr>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP3_LBL_QPlanTitle">Fall 2017  </span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP3$TB_Line1" type="text" value="ENGR 121" maxlength="40" id="QP3_TB_Line1" tabindex="39" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP3_TB_Line1&#39;, &#39;QP3_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP3$TB_Line2" type="text" value=" " maxlength="40" id="QP3_TB_Line2" tabindex="40" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP3_TB_Line2&#39;, &#39;QP3_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP3$TB_Line3" type="text" value=" " maxlength="40" id="QP3_TB_Line3" tabindex="41" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP3_TB_Line3&#39;, &#39;QP3_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP3$TB_Line4" type="text" value=" " maxlength="40" id="QP3_TB_Line4" tabindex="42" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP3_TB_Line4&#39;, &#39;QP3_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP3$TB_Line5" type="text" value=" " maxlength="40" id="QP3_TB_Line5" tabindex="43" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP3_TB_Line5&#39;, &#39;QP4_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP4_LBL_QPlanTitle">Winter 2018</span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP4$TB_Line1" type="text" value="CS 131" maxlength="40" id="QP4_TB_Line1" tabindex="44" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP4_TB_Line1&#39;, &#39;QP4_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP4$TB_Line2" type="text" value=" " maxlength="40" id="QP4_TB_Line2" tabindex="45" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP4_TB_Line2&#39;, &#39;QP4_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP4$TB_Line3" type="text" value=" " maxlength="40" id="QP4_TB_Line3" tabindex="46" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP4_TB_Line3&#39;, &#39;QP4_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP4$TB_Line4" type="text" value=" " maxlength="40" id="QP4_TB_Line4" tabindex="47" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP4_TB_Line4&#39;, &#39;QP4_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP4$TB_Line5" type="text" value=" " maxlength="40" id="QP4_TB_Line5" tabindex="48" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP4_TB_Line5&#39;, &#39;QP5_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
											</tr>
											<tr>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP5_LBL_QPlanTitle">Spring 2018</span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP5$TB_Line1" type="text" value="CS 132" maxlength="40" id="QP5_TB_Line1" tabindex="49" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP5_TB_Line1&#39;, &#39;QP5_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP5$TB_Line2" type="text" value=" " maxlength="40" id="QP5_TB_Line2" tabindex="50" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP5_TB_Line2&#39;, &#39;QP5_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP5$TB_Line3" type="text" value=" " maxlength="40" id="QP5_TB_Line3" tabindex="51" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP5_TB_Line3&#39;, &#39;QP5_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP5$TB_Line4" type="text" value=" " maxlength="40" id="QP5_TB_Line4" tabindex="52" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP5_TB_Line4&#39;, &#39;QP5_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP5$TB_Line5" type="text" value=" " maxlength="40" id="QP5_TB_Line5" tabindex="53" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP5_TB_Line5&#39;, &#39;QP6_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP6_LBL_QPlanTitle">Summer 2018</span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP6$TB_Line1" type="text" value=" " maxlength="40" id="QP6_TB_Line1" tabindex="54" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP6_TB_Line1&#39;, &#39;QP6_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP6$TB_Line2" type="text" value=" " maxlength="40" id="QP6_TB_Line2" tabindex="55" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP6_TB_Line2&#39;, &#39;QP6_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP6$TB_Line3" type="text" value=" " maxlength="40" id="QP6_TB_Line3" tabindex="56" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP6_TB_Line3&#39;, &#39;QP6_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP6$TB_Line4" type="text" value=" " maxlength="40" id="QP6_TB_Line4" tabindex="57" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP6_TB_Line4&#39;, &#39;QP6_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP6$TB_Line5" type="text" value=" " maxlength="40" id="QP6_TB_Line5" tabindex="58" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP6_TB_Line5&#39;, &#39;QP7_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
											</tr>
											<tr>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP7_LBL_QPlanTitle">Fall 2018  </span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP7$TB_Line1" type="text" value="ENGR&amp; 214" maxlength="40" id="QP7_TB_Line1" tabindex="59" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP7_TB_Line1&#39;, &#39;QP7_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP7$TB_Line2" type="text" value=" " maxlength="40" id="QP7_TB_Line2" tabindex="60" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP7_TB_Line2&#39;, &#39;QP7_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP7$TB_Line3" type="text" value=" " maxlength="40" id="QP7_TB_Line3" tabindex="61" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP7_TB_Line3&#39;, &#39;QP7_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP7$TB_Line4" type="text" value=" " maxlength="40" id="QP7_TB_Line4" tabindex="62" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP7_TB_Line4&#39;, &#39;QP7_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP7$TB_Line5" type="text" value=" " maxlength="40" id="QP7_TB_Line5" tabindex="63" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP7_TB_Line5&#39;, &#39;QP8_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP8_LBL_QPlanTitle">Winter 2019</span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP8$TB_Line1" type="text" value="HUM " maxlength="40" id="QP8_TB_Line1" tabindex="64" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP8_TB_Line1&#39;, &#39;QP8_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP8$TB_Line2" type="text" value=" " maxlength="40" id="QP8_TB_Line2" tabindex="65" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP8_TB_Line2&#39;, &#39;QP8_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP8$TB_Line3" type="text" value=" " maxlength="40" id="QP8_TB_Line3" tabindex="66" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP8_TB_Line3&#39;, &#39;QP8_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP8$TB_Line4" type="text" value=" " maxlength="40" id="QP8_TB_Line4" tabindex="67" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP8_TB_Line4&#39;, &#39;QP8_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP8$TB_Line5" type="text" value=" " maxlength="40" id="QP8_TB_Line5" tabindex="68" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP8_TB_Line5&#39;, &#39;QP9_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
											</tr>
											<tr>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP9_LBL_QPlanTitle">Spring 2019</span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP9$TB_Line1" type="text" value="ENGL 230" maxlength="40" id="QP9_TB_Line1" tabindex="69" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP9_TB_Line1&#39;, &#39;QP9_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP9$TB_Line2" type="text" value=" " maxlength="40" id="QP9_TB_Line2" tabindex="70" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP9_TB_Line2&#39;, &#39;QP9_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP9$TB_Line3" type="text" value=" " maxlength="40" id="QP9_TB_Line3" tabindex="71" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP9_TB_Line3&#39;, &#39;QP9_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP9$TB_Line4" type="text" value=" " maxlength="40" id="QP9_TB_Line4" tabindex="72" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP9_TB_Line4&#39;, &#39;QP9_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP9$TB_Line5" type="text" value=" " maxlength="40" id="QP9_TB_Line5" tabindex="73" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP9_TB_Line5&#39;, &#39;QP10_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP10_LBL_QPlanTitle">Summer 2019</span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP10$TB_Line1" type="text" value=" " maxlength="40" id="QP10_TB_Line1" tabindex="74" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP10_TB_Line1&#39;, &#39;QP10_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP10$TB_Line2" type="text" value=" " maxlength="40" id="QP10_TB_Line2" tabindex="75" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP10_TB_Line2&#39;, &#39;QP10_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP10$TB_Line3" type="text" value=" " maxlength="40" id="QP10_TB_Line3" tabindex="76" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP10_TB_Line3&#39;, &#39;QP10_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP10$TB_Line4" type="text" value=" " maxlength="40" id="QP10_TB_Line4" tabindex="77" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP10_TB_Line4&#39;, &#39;QP10_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP10$TB_Line5" type="text" value=" " maxlength="40" id="QP10_TB_Line5" tabindex="78" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP10_TB_Line5&#39;, &#39;QP11_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
											</tr>
											<tr>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP11_LBL_QPlanTitle">Fall 2019  </span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP11$TB_Line1" type="text" value="ENGR 204" maxlength="40" id="QP11_TB_Line1" tabindex="79" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP11_TB_Line1&#39;, &#39;QP11_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP11$TB_Line2" type="text" value=" " maxlength="40" id="QP11_TB_Line2" tabindex="80" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP11_TB_Line2&#39;, &#39;QP11_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP11$TB_Line3" type="text" value=" " maxlength="40" id="QP11_TB_Line3" tabindex="81" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP11_TB_Line3&#39;, &#39;QP11_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP11$TB_Line4" type="text" value=" " maxlength="40" id="QP11_TB_Line4" tabindex="82" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP11_TB_Line4&#39;, &#39;QP11_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP11$TB_Line5" type="text" value=" " maxlength="40" id="QP11_TB_Line5" tabindex="83" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP11_TB_Line5&#39;, &#39;QP12_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP12_LBL_QPlanTitle">Winter 2020</span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP12$TB_Line1" type="text" value="SS" maxlength="40" id="QP12_TB_Line1" tabindex="84" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP12_TB_Line1&#39;, &#39;QP12_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP12$TB_Line2" type="text" value=" " maxlength="40" id="QP12_TB_Line2" tabindex="85" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP12_TB_Line2&#39;, &#39;QP12_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP12$TB_Line3" type="text" value=" " maxlength="40" id="QP12_TB_Line3" tabindex="86" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP12_TB_Line3&#39;, &#39;QP12_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP12$TB_Line4" type="text" value=" " maxlength="40" id="QP12_TB_Line4" tabindex="87" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP12_TB_Line4&#39;, &#39;QP12_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP12$TB_Line5" type="text" value=" " maxlength="40" id="QP12_TB_Line5" tabindex="88" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP12_TB_Line5&#39;, &#39;QP13_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
											</tr>
											<tr>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP13_LBL_QPlanTitle">Spring 2020</span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP13$TB_Line1" type="text" value="" maxlength="40" id="QP13_TB_Line1" tabindex="89" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP13_TB_Line1&#39;, &#39;QP13_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP13$TB_Line2" type="text" value=" " maxlength="40" id="QP13_TB_Line2" tabindex="90" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP13_TB_Line2&#39;, &#39;QP13_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP13$TB_Line3" type="text" value=" " maxlength="40" id="QP13_TB_Line3" tabindex="91" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP13_TB_Line3&#39;, &#39;QP13_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP13$TB_Line4" type="text" value=" " maxlength="40" id="QP13_TB_Line4" tabindex="92" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP13_TB_Line4&#39;, &#39;QP13_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP13$TB_Line5" type="text" value=" " maxlength="40" id="QP13_TB_Line5" tabindex="93" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP13_TB_Line5&#39;, &#39;QP14_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP14_LBL_QPlanTitle">Summer 2020</span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP14$TB_Line1" type="text" value=" " maxlength="40" id="QP14_TB_Line1" tabindex="94" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP14_TB_Line1&#39;, &#39;QP14_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP14$TB_Line2" type="text" value=" " maxlength="40" id="QP14_TB_Line2" tabindex="95" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP14_TB_Line2&#39;, &#39;QP14_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP14$TB_Line3" type="text" value=" " maxlength="40" id="QP14_TB_Line3" tabindex="96" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP14_TB_Line3&#39;, &#39;QP14_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP14$TB_Line4" type="text" value=" " maxlength="40" id="QP14_TB_Line4" tabindex="97" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP14_TB_Line4&#39;, &#39;QP14_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP14$TB_Line5" type="text" value=" " maxlength="40" id="QP14_TB_Line5" tabindex="98" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP14_TB_Line5&#39;, &#39;QP15_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
											</tr>
											<tr>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP15_LBL_QPlanTitle">Fall 2020  </span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP15$TB_Line1" type="text" value=" " maxlength="40" id="QP15_TB_Line1" tabindex="99" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP15_TB_Line1&#39;, &#39;QP15_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP15$TB_Line2" type="text" value=" " maxlength="40" id="QP15_TB_Line2" tabindex="100" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP15_TB_Line2&#39;, &#39;QP15_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP15$TB_Line3" type="text" value=" " maxlength="40" id="QP15_TB_Line3" tabindex="101" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP15_TB_Line3&#39;, &#39;QP15_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP15$TB_Line4" type="text" value=" " maxlength="40" id="QP15_TB_Line4" tabindex="102" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP15_TB_Line4&#39;, &#39;QP15_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP15$TB_Line5" type="text" value=" " maxlength="40" id="QP15_TB_Line5" tabindex="103" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP15_TB_Line5&#39;, &#39;QP16_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP16_LBL_QPlanTitle">Winter 2021</span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP16$TB_Line1" type="text" value=" " maxlength="40" id="QP16_TB_Line1" tabindex="104" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP16_TB_Line1&#39;, &#39;QP16_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP16$TB_Line2" type="text" value=" " maxlength="40" id="QP16_TB_Line2" tabindex="105" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP16_TB_Line2&#39;, &#39;QP16_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP16$TB_Line3" type="text" value=" " maxlength="40" id="QP16_TB_Line3" tabindex="106" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP16_TB_Line3&#39;, &#39;QP16_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP16$TB_Line4" type="text" value=" " maxlength="40" id="QP16_TB_Line4" tabindex="107" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP16_TB_Line4&#39;, &#39;QP16_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP16$TB_Line5" type="text" value=" " maxlength="40" id="QP16_TB_Line5" tabindex="108" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP16_TB_Line5&#39;, &#39;QP17_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
											</tr>
											<tr>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP17_LBL_QPlanTitle">Spring 2021</span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP17$TB_Line1" type="text" value=" " maxlength="40" id="QP17_TB_Line1" tabindex="109" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP17_TB_Line1&#39;, &#39;QP17_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP17$TB_Line2" type="text" value=" " maxlength="40" id="QP17_TB_Line2" tabindex="110" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP17_TB_Line2&#39;, &#39;QP17_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP17$TB_Line3" type="text" value=" " maxlength="40" id="QP17_TB_Line3" tabindex="111" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP17_TB_Line3&#39;, &#39;QP17_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP17$TB_Line4" type="text" value=" " maxlength="40" id="QP17_TB_Line4" tabindex="112" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP17_TB_Line4&#39;, &#39;QP17_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP17$TB_Line5" type="text" value=" " maxlength="40" id="QP17_TB_Line5" tabindex="113" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP17_TB_Line5&#39;, &#39;QP18_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP18_LBL_QPlanTitle">Summer 2021</span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP18$TB_Line1" type="text" value=" " maxlength="40" id="QP18_TB_Line1" tabindex="114" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP18_TB_Line1&#39;, &#39;QP18_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP18$TB_Line2" type="text" value=" " maxlength="40" id="QP18_TB_Line2" tabindex="115" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP18_TB_Line2&#39;, &#39;QP18_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP18$TB_Line3" type="text" value=" " maxlength="40" id="QP18_TB_Line3" tabindex="116" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP18_TB_Line3&#39;, &#39;QP18_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP18$TB_Line4" type="text" value=" " maxlength="40" id="QP18_TB_Line4" tabindex="117" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP18_TB_Line4&#39;, &#39;QP18_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP18$TB_Line5" type="text" value=" " maxlength="40" id="QP18_TB_Line5" tabindex="118" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP18_TB_Line5&#39;, &#39;QP19_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
											</tr>
											<tr>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP19_LBL_QPlanTitle">Fall 2021  </span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP19$TB_Line1" type="text" value=" " maxlength="40" id="QP19_TB_Line1" tabindex="119" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP19_TB_Line1&#39;, &#39;QP19_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP19$TB_Line2" type="text" value=" " maxlength="40" id="QP19_TB_Line2" tabindex="120" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP19_TB_Line2&#39;, &#39;QP19_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP19$TB_Line3" type="text" value=" " maxlength="40" id="QP19_TB_Line3" tabindex="121" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP19_TB_Line3&#39;, &#39;QP19_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP19$TB_Line4" type="text" value=" " maxlength="40" id="QP19_TB_Line4" tabindex="122" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP19_TB_Line4&#39;, &#39;QP19_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP19$TB_Line5" type="text" value=" " maxlength="40" id="QP19_TB_Line5" tabindex="123" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP19_TB_Line5&#39;, &#39;QP20_TB_Line1&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
												<td nowrap="" width="300">
<table width="300" style="BORDER-RIGHT: 1px inset; BORDER-TOP: 1px inset; BORDER-LEFT: 1px inset; BORDER-BOTTOM: 1px inset;" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td id="qp_title" align="center" style="FONT-WEIGHT: bold; FONT-SIZE: 10pt; COLOR: midnightblue; FONT-FAMILY: Arial; BACKGROUND-COLOR: #add8e6" nowrap="">
			<span id="QP20_LBL_QPlanTitle">Winter 2022</span>
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP20$TB_Line1" type="text" value=" " maxlength="40" id="QP20_TB_Line1" tabindex="124" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP20_TB_Line1&#39;, &#39;QP20_TB_Line2&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP20$TB_Line2" type="text" value=" " maxlength="40" id="QP20_TB_Line2" tabindex="125" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP20_TB_Line2&#39;, &#39;QP20_TB_Line3&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP20$TB_Line3" type="text" value=" " maxlength="40" id="QP20_TB_Line3" tabindex="126" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP20_TB_Line3&#39;, &#39;QP20_TB_Line4&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP20$TB_Line4" type="text" value=" " maxlength="40" id="QP20_TB_Line4" tabindex="127" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" onfocus="if (typeof(autojump) != &#39;undefined&#39;) {autojump(&#39;QP20_TB_Line4&#39;, &#39;QP20_TB_Line5&#39;, 40)};" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
	<tr>
		<td nowrap="">
			<input name="QP20$TB_Line5" type="text" value=" " maxlength="40" id="QP20_TB_Line5" tabindex="128" class="textbox_w296_noborder" onchange="if (typeof(SetDirty) != &#39;undefined&#39;) { SetDirty(true); }" style="border-width:0px;border-style:None;height:16px;">
		</td>
	</tr>
</tbody></table></td>
											</tr>
										</tbody></table>
									</td>
								</tr>
							</tbody></table>
						</div>
					</td>
				</tr>
			</tbody></table>
    
<script language="javascript">var arrMsg = [["7508","Are you sure you want to delete this plan?"]];var arrMsgLength=1;</script></form>


</body></html>
''')