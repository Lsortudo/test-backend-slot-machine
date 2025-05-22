import { useState } from 'react';
import axios from 'axios';
import { motion, AnimatePresence } from 'framer-motion';
import { Button } from './UI/Button';
import { SlotReel } from './SlotReel';

interface SpinResult {
  reels: string[];
  win: boolean;
  payout: number;
  message: string;
}

export const SlotMachine = () => {
  const [isSpinning, setIsSpinning] = useState(false);
  const [result, setResult] = useState<SpinResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [credits, setCredits] = useState(100);

  const handleSpin = async () => {
    if (isSpinning || credits < 1) return;

    setIsSpinning(true);
    setError(null);
    setCredits(prev => prev - 1); // Deduct credit before spin

    try {
      const response = await axios.get<SpinResult>('http://localhost:8000/spin', {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        }
      });

      // Simulate spinning animation
      setTimeout(() => {
        setResult(response.data);
        setIsSpinning(false);
        if (response.data.win) {
          setCredits(prev => prev + response.data.payout);
        }
      }, 2000);
    } catch (error) {
      setIsSpinning(false);
      setError('Failed to connect to server. Please try again.');
      setCredits(prev => prev + 1); // Refund credit on error
      setResult(null);
    }
  };

  return (
    <div className="min-h-screen bg-[#1a1a2e] flex items-center justify-center p-4">
      <div className="w-full max-w-2xl">
        <h1 className="text-4xl font-bold text-center text-white mb-8 bg-purple-600/30 py-4 rounded-lg backdrop-blur-sm">
          Double Diamond Slot Machine
        </h1>

        <div className="bg-[#252547] p-8 rounded-xl shadow-2xl">
          <div className="text-white text-xl mb-4 text-center">
            Credits: {credits}
          </div>

          <div className="bg-[#1a1a2e] p-6 rounded-lg mb-8 border-2 border-purple-500/30">
            <div className="flex justify-around gap-4 mb-6">
              {(result?.reels || Array(3).fill('BLANK')).map((symbol, index) => (
                <SlotReel key={index} symbol={symbol} isSpinning={isSpinning} />
              ))}
            </div>

            {error && (
              <div className="text-center text-red-500 font-semibold mb-4">
                {error}
              </div>
            )}

            <Button
              onClick={handleSpin}
              disabled={isSpinning || credits < 1}
              className="bg-red-600 hover:bg-red-700 text-white font-bold py-3 px-8 rounded-full w-40 mx-auto block disabled:bg-red-900"
            >
              {isSpinning ? 'SPINNING...' : credits < 1 ? 'NO CREDITS' : 'SPIN'}
            </Button>
          </div>

          {result && (
            <div className="text-center text-white mb-4">
              {result.message}
            </div>
          )}

          <div className="text-center text-sm text-gray-400">
            Connecting to the backend at localhost:8000/spin (caso eu esqueca de dar run no backend)
          </div>
        </div>

        <div className="text-center mt-4 text-gray-500">
          © 2025 Double Diamond Slots - Teste Técnico BT
        </div>
      </div>
    </div>
  );
};