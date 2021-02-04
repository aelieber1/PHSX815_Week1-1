#include "TRandom.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TH3D.h"
#include "TVector3.h"
#include "TRandom.h"
#include <iostream>

using namespace std;

void Random_ROOT(){

  TRandom random;
  
  TH1D* hist = new TH1D("hist","hist",
			100, -0.1, 1.1);

  int N = 1000000;
  for(int i = 0; i < N; i++){
    hist->Fill(random.Rndm());
  }
  
  hist->Draw();

}
