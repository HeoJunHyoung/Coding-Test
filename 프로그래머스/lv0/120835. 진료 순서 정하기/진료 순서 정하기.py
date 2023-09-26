def solution(emergency):

    
    dictEmer = dict(zip(sorted(emergency, reverse=True), list(range(1, len(emergency)+1) )))
    
    return [dictEmer[i] for i in emergency]