from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Board
from .models import Comment


# Create your views here.

def board(request):
    boards=Board.objects
    board_list=Board.objects.all()
    paginator = Paginator(board_list,5)
    page = request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request, 'board.html',{'boards':boards,'posts':posts})

def boarddetail(request, board_id):
    board_detail=get_object_or_404(Board, pk=board_id)
    if request.method == "POST":
            Comment.objects.create(
                board = board_detail,
                comment_author=request.POST.get('comment_author'),
                comment_contents=request.POST.get('comment_contents'),
            )
            return redirect('/board/boarddetail/'+str(board_detail.id))
    return render(request,'boarddetail.html',{'board':board_detail})

def new(request):
    return render(request, 'new.html')
    
def create(request):
    board = Board()
    board.title = request.GET['title']
    board.name = request.GET['name']
    board.body = request.GET['body']
    board.pub_date = timezone.datetime.now()
    board.save()
    return redirect('board')

def delete(request, board_id):
    board_delete = get_object_or_404(Board,pk=board_id)
    board_delete.delete()
    return redirect('board') 

def update(request,board_id):
    board_update=get_object_or_404(Board,pk=board_id)
    return render(request,'update.html',{"boardupdate":board_update})

def updatesend(request, board_id):
    updatesendboard=get_object_or_404(Board,pk=board_id)
    updatesendboard.title=request.GET['updatetitle']
    updatesendboard.name=request.GET['updatename']
    updatesendboard.body=request.GET['updatebody']
    updatesendboard.pub_date=timezone.datetime.now()
    updatesendboard.save()
    return redirect('board') 


