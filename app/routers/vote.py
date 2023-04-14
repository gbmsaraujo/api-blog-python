from typing import List, Optional
from fastapi import Depends, status, HTTPException, APIRouter, Response
from sqlalchemy.orm import Session
from app.oauth2 import verify_access_token
from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(tags=["Vote"], prefix="/vote")

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote:schemas.Vote, db:Session = Depends(get_db), current_user: schemas.UserResponse = Depends(oauth2.get_current_user)):
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()

    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} has already voted on post {vote.post_id}")

        new_vote = models.Vote(post_id=vote.post_id, user_id= current_user.id)
        db.add(new_vote)
        db.commit()
        db.refresh(new_vote)

        return {"message":"successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message":"successfully deleted vote"}

@router.get("/", response_model=List[schemas.VoteResponse])
def get_votes(db:Session = Depends(get_db)):
    votes = db.query(models.Vote).all()

    return votes
